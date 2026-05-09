# main.py

import sys
from models import Expense
from parser import load_expenses
from reporter import summarize

path = sys.argv[1] if len(sys.argv) > 1 else 'expenses.json'

expenses, error = load_expenses(path)

if error:
	print(f"⚠️  {len(error)} invalid items:")
	for err in error:
		print(f" {err}")
	print()

summarize(expenses)


