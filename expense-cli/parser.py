# parser.py

from pathlib import Path
from typing import Tuple, List
import json
from models import Expense


def load_expenses(path: str) -> tuple[list[Expense], list[dict]]:

	json_string = Path(path).read_text()

	expenses: list[Expense] = []
	wrong_obj: list[dict] = []

	data = json.loads(json_string) 

	for d in data:
		try:
			expense = Expense.model_validate(d)
			expenses.append(expense)
		except Exception as e:
			wrong_obj.append(e)
			

	return expenses, wrong_obj
