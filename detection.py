
from stat import ST_CTIME
import os, sys, time
from moving import moving_file_on_detect
path = '/home/kaustubh/Downloads/'

def mostRecentFile(path):
    all_files = os.listdir(path)
    all_files.sort()
    recent_file_time = 0
    recent_indx = 0
    for index, file in enumerate(all_files):
        file_time = os.stat(path+"/"+file).st_ctime
        if(file_time > recent_file_time):
            recent_file_time = file_time
            recent_indx = index
            
    recent_file = all_files[recent_indx]
    recent_file_path = path+recent_file
    moving_file_on_detect(recent_file_path, recent_file)
    return recent_file_path
    


while True:
    try:
        new_file = mostRecentFile(path)
        time.sleep(1)
    except:
        print("No File Found to move")
        time.sleep(10)