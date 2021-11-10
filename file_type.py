import os

def file_type(path):
    name, extension = os.path.splitext(path)
    return extension