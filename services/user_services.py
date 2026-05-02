
from core.security import verify_pswrd, create_token, hash_pswrd
from database.models import Users
from sqlalchemy import select, or_

def register_sql(data, db):
    verify = db.execute(select(Users.username).where(or_(Users.email == data.email, Users.username == data.username))).all()
    if verify:
            return None
    data.password = hash_pswrd(data.password)
    db.add(Users(username = data.username, email = data.email, password = data.password))
    db.commit()
    return {"info": "Succesful Request"}

def login_sql(form, db):
    show = db.execute(select(Users.password, Users.user_id).where(Users.username == form.username)).all()
    if show:
        data = show[0]
        verify = verify_pswrd(form.password, data[0])
        if verify:
            token = create_token({"sub": data[1]})
            return {"access_token": token, "token_type": "bearer"}
        return None
    return None



    