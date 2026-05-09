# main.py

from models import Expense
from parser import load_expenses

e = load_expenses('./expenses.json')
print(e)