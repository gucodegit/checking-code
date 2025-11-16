from pydantic import BaseModel


class GetAuthSchema(BaseModel):
    id: int
    user_type: str


class BaseAuthSchema(BaseModel):
    fullname: str


class AuthTeacherSchema(BaseAuthSchema):
    pass


class AuthStudentSchema(BaseAuthSchema):
    pass
