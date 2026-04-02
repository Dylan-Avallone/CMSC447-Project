# SQLbackend/models.py
from pydantic import BaseModel

class LoginRequest(BaseModel):
    email: str
    password: str

class LoginResponse(BaseModel):
    success: bool
    message: str

class Department(BaseModel):
    id: int
    name: str

class DepartmentDetail(BaseModel):
    id: int
    name: str
    description: str