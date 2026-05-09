# main.py

import sys
from models import Expense
from parser import load_expenses
from reporter import summarize
from timer import Timer


with Timer():

	path = sys.argv[1] if len(sys.argv) > 1 else 'expenses.json'
	category = sys.argv[2] if len(sys.argv) > 2 else None
	
	expenses, error = load_expenses(path)
	
	if error:
		print(f"⚠️  {len(error)} invalid items:")
		for err in error:
			print(f" {err}")
		print()
	
	summarize(expenses, category)
	
	


