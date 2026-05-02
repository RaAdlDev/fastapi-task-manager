
from fastapi import APIRouter, Depends, HTTPException
from typing import Optional
from schemas.task_schema import Tarea, TareaUpdate
from datetime import date
from core.security import decode
from database.connection import get_db
from sqlalchemy.orm import Session
from services.task_services import add_sql, patch_sql, show_sql, delete_sql, one_task_sql, done_sql, pending_sql, limit_before_sql, sort_limit_sql, sort_created_sql, find_sql, get_stats_sql


router = APIRouter()

@router.get("/tasks", status_code=200 )
async def see( current_u: str = Depends(decode), completed: Optional[bool] = None, pending: Optional[bool] = None, limit_before: Optional[date]= None, sort: Optional[str] = None, search: Optional[str]= None, db: Session = Depends(get_db)):
    if pending:
         return pending_sql(current_u, db)
    elif completed:
         return done_sql(current_u, db)
    elif limit_before:
        return limit_before_sql(limit_before, current_u, db)
    elif sort == "limit":
        return sort_limit_sql(current_u, db)
    elif sort == "created":
        reverse = False
        return sort_created_sql(reverse, current_u, db)
    elif sort == "-created":
        reverse = True
        return sort_created_sql(reverse, current_u, db)
    elif search:
        return find_sql(search, current_u, db)
    else:
        return show_sql(current_u, db)



@router.get("/task/{id}", status_code=200)
async def tsk(id: str, current_u: str = Depends(decode), db: Session = Depends(get_db)):
     verify = one_task_sql(id, current_u, db)
     if verify is None:
         raise HTTPException(status_code= 404, detail="Task Not Found")
     return verify

@router.get("/tasks/stats")
async def stats( current_u: str = Depends(decode), db: Session = Depends(get_db)):
    return get_stats_sql(current_u, db)

@router.post("/tasks", status_code=201)
async def add( tarea: Tarea, current_u: str = Depends(decode), db: Session = Depends(get_db)):
    return add_sql(tarea, current_u, db)

@router.delete("/tasks/{id}", status_code=200)
async def delete(id: str, current_u: str = Depends(decode), db: Session = Depends(get_db)):
    verify =  delete_sql(id, current_u, db)
    if verify is None:
        raise HTTPException(status_code=404, detail="Task Not Found")
    return verify

@router.patch("/tasks/{id}", status_code=200)
async def modify( id: str, datos_nuevos: TareaUpdate, current_u: str = Depends(decode), db: Session = Depends(get_db)):
    verify = patch_sql(id, datos_nuevos, current_u, db)
    if verify is None:
        raise HTTPException(status_code=404, detail="Task Not Found")
    return verify


