from typing import List, Any

from fastapi import Depends, HTTPException
from sqlalchemy import insert, select, update, delete
from sqlalchemy.exc import IntegrityError

from checking_code.core.core_dependency.db_dependency import DBDependency
from checking_code.database.models import Lessons
from checking_code.apps.lessons.schemas import CreateLessonSchema, LessonReturnData


class LessonsManager:
    def __init__(self, db: DBDependency = Depends(DBDependency)) -> None:
        self.db = db
        self.model = Lessons

    async def create_lesson(self, lesson: CreateLessonSchema) -> LessonReturnData:
        async with self.db.get_session() as session:
            query = (
                insert(self.model).values(**lesson.model_dump()).returning(self.model)
            )
            try:
                result = await session.execute(query)
            except IntegrityError:
                raise HTTPException(status_code=400, detail="Invalid data")
            await session.commit()
            lesson_data = result.scalar_one()
            return LessonReturnData.model_validate(lesson_data, from_attributes=True)

    async def get_lesson(self, id: int) -> LessonReturnData:
        async with self.db.get_session() as session:
            query = select(self.model).where(self.model.id == id)
            result = await session.execute(query)
            lesson_data = result.scalar_one_or_none()
            if not (lesson_data):
                raise HTTPException(status_code=404, detail="Lesson not found")
            return LessonReturnData.model_validate(lesson_data, from_attributes=True)

    async def get_lessons(self) -> List[LessonReturnData]:
        async with self.db.get_session() as session:
            query = select(self.model)
            result = await session.execute(query)
            lessons_data = result.scalars().all()
            if not (lessons_data):
                raise HTTPException(status_code=404, detail="Lessons not found")
            return [
                LessonReturnData.model_validate(lesson, from_attributes=True)
                for lesson in lessons_data
            ]

    async def update_lesson_fields(self, id: int, **kwargs: Any) -> LessonReturnData:
        async with self.db.get_session() as session:
            query = (
                update(self.model)
                .where(self.model.id == id)
                .values(**kwargs)
                .returning(self.model)
            )
            try:
                result = await session.execute(query)
            except IntegrityError:
                raise HTTPException(status_code=400, detail="Invalid data")
            await session.commit()
            lesson_data = result.scalar_one_or_none()
            if not (lesson_data):
                raise HTTPException(status_code=404, detail="Lesson not found")
            return LessonReturnData.model_validate(lesson_data, from_attributes=True)

    async def delete_lesson(self, id: int) -> LessonReturnData:
        async with self.db.get_session() as session:
            query = delete(self.model).where(self.model.id == id).returning(self.model)
            result = await session.execute(query)
            await session.commit()
            lesson_data = result.scalar_one_or_none()
            if not (lesson_data):
                raise HTTPException(status_code=404, detail="Lesson not found")
            return LessonReturnData.model_validate(lesson_data, from_attributes=True)
