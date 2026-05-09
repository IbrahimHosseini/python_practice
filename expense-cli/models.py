# models.py

from pydantic import BaseModel, Field
from enum import Enum


class Category(str, Enum):
	food = "Food"
	transport = "Transport"
	rent = "Rent"
	loan = "Loan"
	edu = "Education"
	entertainment = "Entertainment"


class Expense(BaseModel):
	date: str
	amount: float = Field(gt=0)
	category: Category
	description: str


