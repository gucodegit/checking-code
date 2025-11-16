from typing import Annotated

from fastapi import APIRouter, Depends, status
from fastapi.responses import JSONResponse

from checking_code.apps.auth.services import AuthService
from checking_code.apps.auth.depends import get_current_user
from checking_code.apps.auth.schemas import (
    AuthTeacherSchema,
    AuthStudentSchema,
    GetAuthSchema,
)


auth_router = APIRouter(prefix="/auth", tags=["Authentication"])


@auth_router.post(path="/teacher", status_code=status.HTTP_200_OK)
async def auth_teacher(
    teacher: AuthTeacherSchema, service: AuthService = Depends(AuthService)
) -> JSONResponse:
    return await service.auth_teacher(teacher=teacher)


@auth_router.post(path="/student", status_code=status.HTTP_200_OK)
async def auth_student(
    student: AuthStudentSchema, service: AuthService = Depends(AuthService)
) -> JSONResponse:
    return await service.auth_student(student=student)


@auth_router.get(path="/current_user", status_code=status.HTTP_200_OK)
async def get_auth_user(
    user: Annotated[GetAuthSchema, Depends(get_current_user)],
) -> GetAuthSchema:
    return user
