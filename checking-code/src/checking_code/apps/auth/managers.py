from fastapi import Depends, HTTPException
from sqlalchemy import select

from checking_code.core.core_dependency.db_dependency import DBDependency
from checking_code.database.models import Teachers, Students
from checking_code.apps.teachers.schemas import TeacherReturnData
from checking_code.apps.students.schemas import StudentReturnData


class AuthManager:
    def __init__(self, db: DBDependency = Depends(DBDependency)) -> None:
        self.db = db
        self.teacher_model = Teachers
        self.student_model = Students

    async def get_teacher_by_fullname(self, fullname: str) -> TeacherReturnData | None:
        async with self.db.get_session() as session:
            query = select(self.teacher_model).where(
                self.teacher_model.fullname == fullname
            )
            result = await session.execute(query)
            teacher = result.scalar_one_or_none()
            if teacher:
                return TeacherReturnData.model_validate(teacher, from_attributes=True)
            return None

    async def get_student_by_fullname(self, fullname: str) -> StudentReturnData | None:
        async with self.db.get_session() as session:
            query = select(self.student_model).where(
                self.student_model.fullname == fullname
            )
            result = await session.execute(query)
            student = result.scalar_one_or_none()
            if student:
                return StudentReturnData.model_validate(student, from_attributes=True)
            return None
