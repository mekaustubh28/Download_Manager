from stat import ST_CTIME
import os, sys, time
from moving import moving_file_on_detect
path = '/home/kaustubh/Downloads/'

def mostRecentFile(path):
    all_files = os.listdir(path)
    all_files.sort()
    for file in all_files:
        if (file == 'files'):
            pass
        else:
            file_path = path+file
            print(file_path)
            moving_file_on_detect(file_path, file)
        
        return file

while True:
    try:
        new_file = mostRecentFile(path)
        time.sleep(1)
    except:
        print("No File Found to move")
        time.sleep(10)
