from sqlalchemy import select, func
from datetime import datetime
from database.models import Tasks

def to_user(show):
     keys = ["title", "limit", "created", "done", "task_id"]
     return [dict(zip(keys, s)) for s in show]
def date_now():
      return datetime.now().date()

def show_sql(current, db):
     show = db.execute(select(Tasks.title, Tasks.limited, Tasks.created, Tasks.done, Tasks.id ).where(Tasks.user_id == current)).all()
     return to_user(show)

def add_sql( ta, current, db):
         ta.user_id = current
         ta.created = date_now()
         db.add(Tasks(title = ta.title, limited = ta.limit, created= ta.created, done = ta.done, user_id = ta.user_id))
         db.commit()
         return show_sql(current, db)
def patch_sql(id, datos_nuevos, current, db):
          verify = db.execute(select(Tasks).where(Tasks.id == id, Tasks.user_id == current)).all()
          if verify:
               user = db.get(Tasks, id)
               if datos_nuevos.title:
                    user.title = datos_nuevos.title
               if datos_nuevos.limit:
                    user.limited = datos_nuevos.limit
               if not datos_nuevos.done is None:
                    user.done = datos_nuevos.done
               db.commit()
               return show_sql(current, db)
          return None

def delete_sql( id, current, db):
     verify = db.execute(select(Tasks).where(Tasks.id == id, Tasks.user_id == current)).all()
     if verify:
          task_out = db.get(Tasks, id)
          db.delete(task_out)
          db.commit()
          return show_sql(current, db)
     return None
def one_task_sql(id, current, db):
     show = db.execute(select(Tasks.title, Tasks.limited, Tasks.created, Tasks.done, Tasks.id).where(Tasks.user_id == current, Tasks.id == id)).all()
     if show:
          return to_user(show)
     return None
    
def done_sql(current, db):
     show = db.execute(select(Tasks.title, Tasks.limited, Tasks.created, Tasks.done, Tasks.id).where(Tasks.user_id == current, Tasks.done == 1)).all()
     return to_user(show)

def pending_sql(current, db):
     show = db.execute(select(Tasks.title, Tasks.limited, Tasks.created, Tasks.done, Tasks.id).where(Tasks.user_id == current, Tasks.done == 0)).all()
     return to_user(show)
def limit_before_sql(limit_b, current, db):
     show = db.execute(select(Tasks.title, Tasks.limited, Tasks.created, Tasks.done, Tasks.id).where(Tasks.user_id == current, Tasks.limited < limit_b)).all()
     return to_user(show)
def sort_limit_sql(current, db): 
     show = db.execute(select(Tasks.title, Tasks.limited, Tasks.created, Tasks.done, Tasks.id).where(Tasks.user_id == current).order_by(Tasks.limited)).all()
     return to_user(show)
def sort_created_sql(r, current, db):
     if r:
          show = db.execute(select(Tasks.title, Tasks.limited, Tasks.created, Tasks.done, Tasks.id).where(Tasks.user_id == current).order_by(Tasks.created.desc())).all()
          return to_user(show)
     else: 
          show = db.execute(select(Tasks.title, Tasks.limited, Tasks.created, Tasks.done, Tasks.id).where(Tasks.user_id == current).order_by(Tasks.created)).all()
          return to_user(show)
def find_sql(search, current, db):
     show = db.execute(select(Tasks.title, Tasks.limited, Tasks.created, Tasks.done, Tasks.id).where(Tasks.user_id == current, Tasks.title.ilike(f"%{search}%") )).all()
     return to_user(show)
def get_stats_sql(current, db):
     completed = db.execute(select(func.count("*")).where(Tasks.user_id == current, Tasks.done == 1)).first()
     total = db.execute(select(func.count("*")).where(Tasks.user_id == current,)).first()
     return  {"total": total[0], "completed": completed[0], "pending": total[0] - completed[0]}



       


         
         
         

