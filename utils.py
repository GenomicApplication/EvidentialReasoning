__author__ = 'tami'

DEBUG = False

try: input = raw_input
except NameError: pass

def dprint(str):
    if DEBUG:
        print(str)