# main.py

from models import Expense
from parser import load_expenses
from reporter import summarize

expenses, error = load_expenses('./expenses.json')
# print(e)

summarize(expenses)
