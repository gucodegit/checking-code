from fastapi import FastAPI
from pydantic import BaseModel
from typing import Optional
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

# CORS middleware
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:8080"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

class SimpleLesson(BaseModel):
    lesson_date: str
    lesson_time: str
    assignment_number: str
    assignment_description: Optional[str] = None
    attachment_path: Optional[str] = None
    assignment_deadline: Optional[str] = None
    group_id: int
    subject_id: int

@app.post("/lessons")
async def create_lesson(lesson: SimpleLesson):
    print(f"✅ Получен запрос: {lesson.model_dump()}")
    
    # Возвращаем тестовые данные
    return {
        "message": "Успешно! (тестовый режим)",
        "lesson_id": 123,
        "lesson_date": lesson.lesson_date,
        "lesson_time": lesson.lesson_time,
        "assignment_number": lesson.assignment_number,
        "assignment_description": lesson.assignment_description,
        "attachment_path": lesson.attachment_path,
        "assignment_deadline": lesson.assignment_deadline,
        "group_id": lesson.group_id,
        "subject_id": lesson.subject_id
    }

# Эндпоинт для проверки
@app.get("/")
async def root():
    return {"message": "Test API is running"}

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)