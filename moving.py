import shutil, os
from file_type import file_type

def moving_file_on_detect(src, name):
    try:
        file_extension = file_type(src)
        if (len(file_extension) == 0):
            dst = '/home/kaustubh/personal/python/clustering/files/Folders/'
        else:
            file_extension = file_extension[1:]
            if (file_extension == 'py' or file_extension == 'txt' or file_extension == 'csv'):
                dst = '/home/kaustubh/personal/python/clustering/files/Files/'
            elif (file_extension == 'pdf'):
                dst = '/home/kaustubh/personal/python/clustering/files/Documents/'
            elif (file_extension == 'jpeg' or file_extension == 'jpg' or file_extension == 'png'):
                dst = '/home/kaustubh/personal/python/clustering/files/Images/'
            elif (file_extension == 'mp4'):
                dst = '/home/kaustubh/personal/python/clustering/files/Videos/'
            elif (file_extension == 'mp3'):
                dst = '/home/kaustubh/personal/python/clustering/files/Audios/'
            elif (file_extension == 'zip' or file_extension == 'gz' or file_extension == 'sh' or file_extension == 'deb'):
                dst = '/home/kaustubh/personal/python/clustering/files/Compressed/'
            else:
                dst = '/home/kaustubh/personal/python/clustering/files/Others/'
        dst_file = dst + name
        os.makedirs(os.path.dirname(dst), exist_ok=True)
        shutil.move(src, dst_file)
        print(f'{name} moved successfully')
    except:
        print("Something went wrong")