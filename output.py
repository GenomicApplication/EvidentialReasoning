from utils import *

OUTPUT_FILENAME = ''
FILE_MODE ='a'

def get_filename():

    global OUTPUT_FILENAME

    if OUTPUT_FILENAME == '':
        OUTPUT_FILENAME = str(input("What would you like to name your output txt file? "))
    return OUTPUT_FILENAME

def file_write(str):
    output = open(get_filename(), FILE_MODE)
    output.write(str)
    output.close()



