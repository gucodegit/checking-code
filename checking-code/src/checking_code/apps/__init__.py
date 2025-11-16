from fastapi import APIRouter

from checking_code.apps.teachers.routes import teachers_router
from checking_code.apps.students.routes import students_router
from checking_code.apps.groups.routes import groups_router
from checking_code.apps.subjects.routes import subjects_router
from checking_code.apps.lessons.routes import lessons_router
from checking_code.apps.assignments.routes import assignments_router
from checking_code.apps.auth.routes import auth_router


apps_router = APIRouter(prefix="/api/v1")

apps_router.include_router(router=teachers_router)
apps_router.include_router(router=students_router)
apps_router.include_router(router=groups_router)
apps_router.include_router(router=subjects_router)
apps_router.include_router(router=lessons_router)
apps_router.include_router(router=assignments_router)
apps_router.include_router(router=auth_router)
