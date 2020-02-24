# Imports to inspect / modify directories
import os
import json
import time

# String to declare the user name of the Windows account
username = "Alex Maclean"

# String to declare the folder to sort
sourceFolder = "C:/Users/" + username + "/Downloads"

# String to declare header for beginning of file name (optional)
fileHeader = ""

# Lists to declare file extensions for each folder
desktopExtensions = ["exe", "bin"]
documentExtensions = ["txt", "doc", "docx", "odt", "pdf", "rtf", "htm", "html", "xls", "xlsx", "ppt", "pptx", "css", "js", "py", "java", "zip"]
pictureExtensions = ["jpg", "png", "jpeg", "bmp", "jfif", "gif", "tiff", "svg"]
videoExtensions = ["avi", "mp4", "wmv", "mov", "flv"]
audioExtensions = ["mp3", "wav", "bwf", "aiff", "wma"]

# Function to sort the files of a specified folder
def file_sorter(sourceFolder):
    # Loop to iterate through every file in the folder
    for file in os.listdir(sourceFolder):
        # If statement to exclude folders / default file and split other files into names and extensions
        if (file == "desktop.ini" or not("." in file)):
            continue
        else:
            fileNameExtension = file.split(".")
        # If statement to assign destination folder based on file type
        if (fileNameExtension[-1] in desktopExtensions):
            destinationFolder = "C:/Users/" + username + "/Desktop"
        elif (fileNameExtension[-1] in documentExtensions):
            destinationFolder = "C:/Users/" + username + "/Documents"
        elif (fileNameExtension[-1] in pictureExtensions):
            destinationFolder = "C:/Users/"+ username + "/Pictures"
        elif (fileNameExtension[-1] in videoExtensions):
            destinationFolder = "C:/Users/" + username + "/Videos"
        elif (fileNameExtension[-1] in audioExtensions):
            destinationFolder = "C:/Users/" + username + "/Music"
        else:
            destinationFolder = "C:/Users/" + username + "/Documents"
        # Strings to declare the source, destination, and header (if applicable) of the file
        source = sourceFolder + "/" + file
        destination = destinationFolder + "/" + fileHeader + file
        # OS Rename function to move the file from one folder to the other
        os.rename(source, destination)

file_sorter(sourceFolder)