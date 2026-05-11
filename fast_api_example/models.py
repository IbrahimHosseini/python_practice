# models.py

from pydantic import BaseModel, Field
from typing import Optional


# request model
class CreateUserRequest(BaseModel):
	name: str
	age: int
	email: str

# Update request model
class UpdateUserRequest(BaseModel):
	name: Optional[str] = None
	age: Optional[int] = Field(None, gt=0, lt=150)
	email: Optional[str] = None

# response model
class UserResponse(BaseModel):
	id: int
	name: str
	age: int = Field(gt=0, lt=150)
	email: str


# error model
class ErrorResponse(BaseModel):
	code: str # "USER_NOT_FOUND"
	message: str


