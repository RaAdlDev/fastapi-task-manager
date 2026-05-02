from pydantic import BaseModel, EmailStr



class User(BaseModel):
    username: str
    email: EmailStr

class UserDB(User):
    password: str

