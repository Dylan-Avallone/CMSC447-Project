from fastapi import FastAPI, HTTPException
from models import LoginRequest, LoginResponse, Department, DepartmentDetail
from auth import authenticate
from data import departments, department_info

app = FastAPI(title="Library Dashboard Prototype")

# --- Authentication endpoint ---
@app.post("/login", response_model=LoginResponse)
def login(request: LoginRequest):
    if authenticate(request.email, request.password):
        return LoginResponse(success=True, message="Login successful")
    else:
        raise HTTPException(status_code=401, detail="Invalid email or password")

# --- Get list of departments ---
@app.get("/departments", response_model=list[Department])
def get_departments():
    return departments

# --- Get department details ---
@app.get("/departments/{dept_id}", response_model=DepartmentDetail)
def get_department_detail(dept_id: int):
    dept = next((d for d in departments if d["id"] == dept_id), None)
    if not dept:
        raise HTTPException(status_code=404, detail="Department not found")
    info = department_info.get(dept_id, {})
    return DepartmentDetail(id=dept["id"], name=dept["name"], description=info.get("description", ""))
