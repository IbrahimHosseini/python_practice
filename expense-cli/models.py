# models.py

from pydantic import BaseModel, Field
from enum import Enum
from datetime import date


class Category(str, Enum):
	food = "Food"
	transport = "Transportation"
	rent = "Rent"
	loan = "Loan"
	edu = "Education"
	entertainment = "Entertainment"


class Expense(BaseModel):
	date: date
	amount: float = Field(gt=0)
	category: Category
	description: str


