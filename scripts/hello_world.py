# Import section
import os
import sys

def print_message(message):
	my_message = f"[Message]: {message}"
	os.system(f"echo {my_message}")

print_message(sys.argv[-1])
