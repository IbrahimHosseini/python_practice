# timer.py

import time


class Timer:

	def __enter__(self):
		self.start = time.time()
		return self

	def __exit__(self, *args):
		end = time.time()
		elapsed = end - self.start
	
		print()
		print(f"Execuation time: {elapsed:.3f} seconds\n")