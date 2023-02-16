import os, sys
try:
    __import__("SPI3ER_enc").menu()
except Exception as e:
    exit(str(e))
