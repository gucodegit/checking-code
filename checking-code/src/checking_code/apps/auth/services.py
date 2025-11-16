from fastapi import Depends, HTTPException, status
from fastapi.responses import JSONResponse

from checking_code.core.settings import settings
from checking_code.apps.auth.managers import AuthManager
from checking_code.apps.auth.utils import AuthUtil
from checking_code.apps.auth.schemas import AuthTeacherSchema, AuthStudentSchema


class AuthService:
    def __init__(
        self,
        manager: AuthManager = Depends(AuthManager),
        util: AuthUtil = Depends(AuthUtil),
    ) -> None:
        self.manager = manager
        self.util = util

    async def auth_teacher(self, teacher: AuthTeacherSchema) -> JSONResponse:
        exist_teacher = await self.manager.get_teacher_by_fullname(
            fullname=teacher.fullname
        )
        if not (exist_teacher):
            raise HTTPException(
                status_code=status.HTTP_401_UNAUTHORIZED, detail="Authorization denied"
            )
        token = await self.util.create_access_token(
            user_id=exist_teacher.id, user="teacher"
        )
        response = JSONResponse(
            content={"message": "Success authorization for teacher"}
        )
        response.set_cookie(
            key="Authorization",
            value=token,
            httponly=True,
            max_age=settings.access_token_expire,
        )
        return response

    async def auth_student(self, student: AuthStudentSchema) -> JSONResponse:
        exist_student = await self.manager.get_student_by_fullname(
            fullname=student.fullname
        )
        if not (exist_student):
            raise HTTPException(
                status_code=status.HTTP_401_UNAUTHORIZED, detail="Authorization denied"
            )
        token = await self.util.create_access_token(
            user_id=exist_student.id, user="student"
        )
        response = JSONResponse(
            content={"message": "Success authorization for student"}
        )
        response.set_cookie(
            key="Authorization",
            value=token,
            httponly=True,
            max_age=settings.access_token_expire,
        )
        return response
