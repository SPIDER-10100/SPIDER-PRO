import os, sys
try:
    __import__("SPIDER").menu()
except Exception as e:
    exit(str(e))
