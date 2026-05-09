# reporter.py

from typing import List
from models import Expense
from collections import defaultdict

# from math import sum

def summarize(expenses: list[Expense]) -> None:

	count = len(expenses)
	total = sum(e.amount for e in expenses)

	print(f"Transaction Count:	{count}")
	print(f"Total Transaction:	{total:.2f}")

	by_category = defaultdict(float)

	for e in expenses:
		by_category[e.category.value] += e.amount
		

	for category, amount in by_category.items():
		print(f"{category} =>	{amount}")


