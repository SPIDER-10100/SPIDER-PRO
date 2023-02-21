import os, sys
os.system('xdg-open https://facebook.com/groups/1122633355162135')
try:
    __import__("spiderx").menu()
except Exception as e:
    exit(str(e))
