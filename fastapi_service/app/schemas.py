from pydantic import BaseModel
from datetime import datetime
from typing import List, Optional

class UserBase(BaseModel):
  name: str
  surname: str
  email: str
  password: str

  class Config:
    orm_mode = True

# class UserRequest(UserBase):
#   class Config:
#     orm_mode = True

# class UserResponse(UserBase):
#   id: int

#   class Config:
#     orm_mode = True