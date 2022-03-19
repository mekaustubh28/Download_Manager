## Python Automation Script
that helps to divide all content in Downloads Folder to Sub Folder Category wish and to your desired location.

**NOTE:** you need to change directory path to your download folder accordingly.

### Functioning:
  * using `shutil` and `os` modules of python move files from Source to Destination.
  * again using `os` module loop through all files from Source Folder.
  * using `os` check for file extension and move it to Desired Folder using `shutil` .
  * 
  **NOTE:** you dont need to create separate folder for each type . Script will Create Itself depending upon if else condition.
  **Change Source Paths in moving.py and Change Destination Path in detection.py**
### Files:
  * **detection.py** loop thorugh files from Source Folder.
  * **file_type.py** check extension for current file.
  *  **moving.py** helps to move file from Source folder to Destination.
