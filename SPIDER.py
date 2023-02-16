import os, sys
try:
    __import__("SPIDER_enc").menu()
except Exception as e:
    exit(str(e))