from pydantic import BaseModel, EmailStr

class Message(BaseModel):
    message: str

class UserSchema(BaseModel):
    usarname: str
    email: EmailStr
    password: str

class UserDB(UserSchema):
    id: int

class UserPublic(BaseModel):
    id: int
    usarname: str
    email: EmailStr