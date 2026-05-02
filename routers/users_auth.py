from schemas.user_schema import UserDB
from fastapi import APIRouter, Depends, HTTPException
from fastapi.security import OAuth2PasswordRequestForm
from services.user_services import register_sql, login_sql
from sqlalchemy.orm import Session
from database.connection import get_db


router = APIRouter()
@router.post("/login")
async def login(form: OAuth2PasswordRequestForm = Depends(), db: Session = Depends(get_db)):
    verify =  login_sql(form, db)
    if verify is None:
        raise HTTPException(status_code=401, detail="Unauthorized")
    return verify
    

@router.post("/register")
async def register(data: UserDB, db: Session = Depends(get_db)):
    verify =  register_sql(data, db)
    if verify is None:
        raise HTTPException(status_code=409, detail="Unauthorized")
    return verify
    
