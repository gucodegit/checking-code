from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from typing import Optional, List
import psycopg2
from psycopg2.extras import RealDictCursor
from dotenv import load_dotenv
import os
import traceback
import logging
# ==========================================================
# 1-я версия 
# - Добавить новое занятие, Список всех занятий
# - Нет методов для таблицы edudb.assignments
# ==========================================================

# Настройка логирования
logging.basicConfig(level=logging.DEBUG)
logger = logging.getLogger(__name__)

# Загрузка переменных окружения
load_dotenv()

app = FastAPI(title="Lesson Management API")

# CORS middleware
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Модели Pydantic
class Group(BaseModel):
    group_id: int
    group_name: str

class Subject(BaseModel):
    subject_id: int
    subject_name: str
    teacher_id: int

class LessonCreate(BaseModel):
    lesson_date: str
    lesson_time: str
    assignment_number: str
    assignment_description: Optional[str] = None
    attachment_path: Optional[str] = None
    assignment_deadline: Optional[str] = None
    group_id: int
    subject_id: int

class Lesson(LessonCreate):
    lesson_id: int

# Подключение к базе данных
def get_db_connection():
    conn = psycopg2.connect(
        host=os.getenv("DB_HOST", "localhost"),
        database=os.getenv("DB_NAME", "dvdrental"),
        user=os.getenv("DB_USER", "postgres"),
        password=os.getenv("DB_PASSWORD", ""),
        cursor_factory=RealDictCursor
    )
    return conn

# Эндпоинты
@app.get("/")
async def root():
    return {"message": "Lesson Management API"}

@app.get("/groups", response_model=List[Group])
async def get_groups():
    conn = get_db_connection()
    cursor = conn.cursor()
    try:
        cursor.execute("SELECT group_id, group_name FROM edudb.groups ORDER BY group_name")
        groups = cursor.fetchall()
        return groups
    except Exception as e:
        logger.error(f"Error in /groups: {str(e)}")
        raise HTTPException(status_code=500, detail=f"Database error: {str(e)}")
    finally:
        cursor.close()
        conn.close()

@app.get("/subjects", response_model=List[Subject])
async def get_subjects():
    conn = get_db_connection()
    cursor = conn.cursor()
    try:
        cursor.execute("""
            SELECT s.subject_id, s.subject_name, s.teacher_id 
            FROM edudb.subjects s 
            ORDER BY s.subject_name
        """)
        subjects = cursor.fetchall()
        return subjects
    except Exception as e:
        logger.error(f"Error in /subjects: {str(e)}")
        raise HTTPException(status_code=500, detail=f"Database error: {str(e)}")
    finally:
        cursor.close()
        conn.close()

@app.get("/teachers")
async def get_teachers():
    conn = get_db_connection()
    cursor = conn.cursor()
    try:
        cursor.execute("SELECT teacher_id, full_name FROM edudb.teachers ORDER BY full_name")
        teachers = cursor.fetchall()
        return teachers
    except Exception as e:
        logger.error(f"Error in /teachers: {str(e)}")
        raise HTTPException(status_code=500, detail=f"Database error: {str(e)}")
    finally:
        cursor.close()
        conn.close()

@app.post("/lessons")
async def create_lesson(lesson: LessonCreate):
    conn = None
    cursor = None
    try:
        logger.info(f"📨 Received lesson creation request: {lesson.model_dump()}")
        
        conn = get_db_connection()
        cursor = conn.cursor()
        
        # Проверяем существование задания с таким номером
        cursor.execute(
            "SELECT assignment_number FROM edudb.lessons WHERE assignment_number = %s",
            (lesson.assignment_number,)
        )
        existing = cursor.fetchone()
        if existing:
            logger.warning(f"Assignment number {lesson.assignment_number} already exists")
            raise HTTPException(
                status_code=400, 
                detail="Assignment number already exists"
            )

        # Обрабатываем пустые значения
        assignment_deadline = lesson.assignment_deadline if lesson.assignment_deadline else None
        assignment_description = lesson.assignment_description if lesson.assignment_description else None
        attachment_path = lesson.attachment_path if lesson.attachment_path else None

        logger.info("🔄 Executing INSERT into database")
        
        # Вставляем новое занятие
        cursor.execute("""
            INSERT INTO edudb.lessons 
            (lesson_date, lesson_time, assignment_number, assignment_description, 
             attachment_path, assignment_deadline, group_id, subject_id)
            VALUES (%s, %s, %s, %s, %s, %s, %s, %s)
            RETURNING lesson_id, lesson_date, lesson_time, assignment_number, 
                      assignment_description, attachment_path, assignment_deadline, 
                      group_id, subject_id
        """, (
            lesson.lesson_date,
            lesson.lesson_time,
            lesson.assignment_number,
            assignment_description,
            attachment_path,
            assignment_deadline,
            lesson.group_id,
            lesson.subject_id
        ))
        
        new_lesson = cursor.fetchone()
        conn.commit()
        
        # Преобразуем даты в строки для корректного JSON
        if new_lesson['lesson_date']:
            new_lesson['lesson_date'] = str(new_lesson['lesson_date'])
        if new_lesson['assignment_deadline']:
            new_lesson['assignment_deadline'] = str(new_lesson['assignment_deadline'])
        
        logger.info(f"✅ Lesson created successfully: {new_lesson}")
        return new_lesson
        
    except HTTPException as he:
        logger.error(f"🚨 HTTPException: {he.detail}")
        if conn:
            conn.rollback()
        raise
    except Exception as e:
        logger.error(f"💥 Critical error in create_lesson: {str(e)}")
        logger.error(f"🔍 Traceback: {traceback.format_exc()}")
        if conn:
            conn.rollback()
        raise HTTPException(status_code=500, detail=f"Server error: {str(e)}")
    finally:
        if cursor:
            cursor.close()
        if conn:
            conn.close()

@app.get("/lessons")
async def get_lessons(limit: int = 100, offset: int = 0):
    conn = get_db_connection()
    cursor = conn.cursor()
    try:
        cursor.execute("""
            SELECT lesson_id, lesson_date, lesson_time, assignment_number, 
                   assignment_description, attachment_path, assignment_deadline, 
                   group_id, subject_id
            FROM edudb.lessons 
            ORDER BY lesson_date DESC, lesson_time DESC
            LIMIT %s OFFSET %s
        """, (limit, offset))
        lessons = cursor.fetchall()
        
        # Преобразуем даты в строки
        for lesson in lessons:
            if lesson['lesson_date']:
                lesson['lesson_date'] = str(lesson['lesson_date'])
            if lesson['assignment_deadline']:
                lesson['assignment_deadline'] = str(lesson['assignment_deadline'])
                
        return lessons
    except Exception as e:
        logger.error(f"Error in /lessons: {str(e)}")
        raise HTTPException(status_code=500, detail=f"Database error: {str(e)}")
    finally:
        cursor.close()
        conn.close()

@app.get("/lessons-detailed")
async def get_lessons_detailed():
    """Получить подробный список всех занятий с информацией о группах и предметах"""
    conn = get_db_connection()
    cursor = conn.cursor()
    try:
        cursor.execute("""
            SELECT 
                l.lesson_id,
                l.lesson_date,
                l.lesson_time,
                l.assignment_number,
                l.assignment_description,
                l.attachment_path,
                l.assignment_deadline,
                g.group_name,
                s.subject_name,
                t.full_name as teacher_name
            FROM edudb.lessons l
            JOIN edudb.groups g ON l.group_id = g.group_id
            JOIN edudb.subjects s ON l.subject_id = s.subject_id
            JOIN edudb.teachers t ON s.teacher_id = t.teacher_id
            ORDER BY l.lesson_date DESC, l.lesson_time DESC
        """)
        lessons = cursor.fetchall()
        return lessons
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Database error: {str(e)}")
    finally:
        cursor.close()
        conn.close()

# if __name__ == "__main__":
#     import uvicorn
#     uvicorn.run(app, host="0.0.0.0", port=8000)
