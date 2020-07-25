import zipfile
import shutil, os
from pathlib import Path
p = Path.home()
shutil.copy(p / 'spam.txt', p / 'some_folder')

shutil.copy(p / 'eggs.txt', p / 'some_folder/eggs2.txt')

# The first shutil.copy() call copies the file at C:\Users\Al\spam.txt to the folder C:\Users\Al\some_folder. The return value is the path of the newly copied file. Note that since a folder was specified as the destination ➊, the original spam.txt filename is used for the new, copied file’s filename. The second shutil.copy() call ➋ also copies the file at C:\Users\Al\eggs.txt to the folder C:\Users\Al\some_folder but gives the copied file the name eggs2.txt.While shutil.copy() will copy a single file, shutil.copytree() will copy an entire folder and every folder and file contained in it. Calling shutil.copytree(source, destination) will copy the folder at the path source, along with all of its files and subfolders, to the folder at the path destination. The source and destination parameters are both strings. The function returns a string of the path of the copied folder.

#--------------------------------------------------------------------

# While shutil.copy() will copy a single file, shutil.copytree() will copy an entire folder and every folder and file contained in it. Calling shutil.copytree(source, destination) will copy the folder at the path source, along with all of its files and subfolders, to the folder at the path destination. The source and destination parameters are both strings. The function returns a string of the path of the copied folder.

# Enter the following into the interactive shell:

import shutil, os
from pathlib import Path
p = Path.home()
shutil.copytree(p / 'spam', p / 'spam_backup')

# The shutil.copytree() call creates a new folder named spam_backup with the same content as the original spam folder. You have now safely backed up your precious, precious spam.

# Moving and Renaming Files and Folders
# Calling shutil.move(source, destination) will move the file or folder at the path source to the path destination and will return a string of the absolute path of the new location.

# If destination points to a folder, the source file gets moved into destination and keeps its current filename. For example, enter the following into the interactive shell:

import shutil

shutil.move('C:\\test\\bacon.txt', 'C:\\test1\\')

# Assuming a folder named eggs already exists in the C: \ directory, this shutil.move() call says, “Move C: \bacon.txt into the folder C: \eggs.”

# If there had been a bacon.txt file already in C: \eggs, it would have been overwritten. Since it’s easy to accidentally overwrite files in this way, you should take some care when using move().

# The destination path can also specify a filename. In the following example, the source file is moved and renamed.

import shutil

shutil.move('C:\\test\\bacon.txt', 'C:\\test1\\new_bacon.txt')

# Finally, the folders that make up the destination must already exist, or else Python will throw an exception. Enter the following into the interactive shell:

import shutil
shutil.move('C:\\test\\bacon.txt', 'C:\\folder_notThere')

#--------------------------------------------------------

##Permanently Deleting Files and Folders
# You can delete a single file or a single empty folder with functions in the os module, whereas to delete a folder and all of its contents, you use the shutil module.

# Calling os.unlink(path) will delete the file at path.
# Calling os.rmdir(path) will delete the folder at path. This folder must be empty of any files or folders.
# Calling shutil.rmtree(path) will remove the folder at path, and all files and folders it contains will also be deleted.

# Using send2trash is much safer than Python’s regular delete functions, because it will send folders and files to your computer’s trash or recycle bin instead of permanently deleting them. If a bug in your program deletes something with send2trash you didn’t intend to delete, you can later restore it from the recycle bin.

# After you have installed send2trash, enter the following into the interactive shell:


import send2trash
bacon_file = open('baconFile.txt', 'a')
bacon_file.write('Bacon is not a vegetable')
bacon_file.close()
send2trash.send2trash('C:\\test1\\baconfile.txt')

# In general, you should always use the send2trash.send2trash() function to delete files and folders. But while sending files to the recycle bin lets you recover them later, it will not free up disk space like permanently deleting them does. If you want your program to free up disk space, use the os and shutil functions for deleting files and folders. Note that the send2trash() function can only send files to the recycle bin
# it cannot pull files out of it.

#----WALKING A DIRECTORY TREE--------------------------------

# Here is an example program that uses the os.walk() function on the directory tree

import os

for folderName, subfolders, fileName in os.walk('C:\\GitRepo'):
    print('The current folder name is' + folderName)

    for subfolder in subfolders:
        print('SUBFOLDER OF ' + folderName + ':' + subfolder)

    for fileNames in fileName:
        print('FILE INSIDE ' + folderName + ':' + fileName)

    print('')


# Since os.walk() returns lists of strings for the subfolder and filename variables, you can use these lists in their own for loops. Replace the print() function calls with your own custom code. (Or if you don’t need one or both of them, remove the for loops.)


#########ZipFiles------------------------------------------------------------


os.chdir('C:\\test')


p = Path(r'C:\test')

example_file = zipfile.ZipFile(p / 'CourseBooks (2).zip')

print(example_file.namelist())

spam_info = example_file.getinfo('CourseBooks/Day2.ipynb')

print(spam_info.file_size)

print(spam_info.compress_type)

print(
    f'Compressed file is {round(spam_info.file_size / spam_info.compress_size, 2)}x smaller!')

# A ZipFile object has a namelist() method that returns a list of strings for all the files and folders contained in the ZIP file. These strings can be passed to the getinfo() ZipFile method to return a ZipInfo object about that particular file. ZipInfo objects have their own attributes, such as file_size and compress_size in bytes, which hold integers of the original file size and compressed file size, respectively. While a ZipFile object represents an entire archive file, a ZipInfo object holds useful information about a single file in the archive.

# The command at ➊ calculates how efficiently example.zip is compressed by dividing the original file size by the compressed file size and prints this information.

# Reading ZIP Files
# To read the contents of a ZIP file, first you must create a ZipFile object(note the capital letters Z and F). ZipFile objects are conceptually similar to the File objects you saw returned by the open() function in the previous chapter: they are values through which the program interacts with the file. To create a ZipFile object, call the zipfile.ZipFile() function, passing it a string of the .ZIP file’s filename. Note that zipfile is the name of the Python module, and ZipFile() is the name of the function.

##---------------------------------------------------------------------
# Extracting from ZIP Files
# The extractall() method for ZipFile objects extracts all the files and folders from a ZIP file into the current working directory.

import zipfile, os

from pathlib import Path

p = Path(r'C:\test')

example_zip = zipfile.ZipFile(p / 'CourseBooks (2).zip')
example_zip.extractall('C:\\test\\ExtractedCourseBooks')
example_zip.extract('CourseBooks/Day4.ipynb', 'C:\\test\\OneExtractedFile')
example_zip.close()

# After running this code, the contents of example.zip will be extracted to C: \. Optionally, you can pass a folder name to extractall() to have it extract the files into a folder other than the current working directory. If the folder passed to the extractall() method does not exist, it will be created. For instance, if you replaced the call at ➊ with exampleZip.extractall('C:\\delicious'), the code would extract the files from example.zip into a newly created C: \delicious folder.

# The extract() method for ZipFile objects will extract a single file from the ZIP file. Continue the interactive shell example:

# The string you pass to extract() must match one of the strings in the list returned by namelist(). Optionally, you can pass a second argument to extract() to extract the file into a folder other than the current working directory. If this second argument is a folder that doesn’t yet exist, Python will create the folder. The value that extract() returns is the absolute path to which the file was extracted.

# Creating and Adding to ZIP Files------------------------###################
# To create your own compressed ZIP files, you must open the ZipFile object in write mode by passing 'w' as the second argument. (This is similar to opening a text file in write mode by passing 'w' to the open() function.)

# When you pass a path to the write() method of a ZipFile object, Python will compress the file at that path and add it into the ZIP file. The write() method’s first argument is a string of the filename to add. The second argument is the compression type parameter, which tells the computer what algorithm it should use to compress the files
# you can always just set this value to zipfile.ZIP_DEFLATED. (This specifies the deflate compression algorithm, which works well on all types of data.) Enter the following into the interactive shell:


print(os.getcwd())
os.chdir('C:\\test')
print(os.getcwd())

new_zip = zipfile.ZipFile('newZip.zip', 'w')
new_zip.write('spam.txt', compress_type=zipfile.ZIP_DEFLATED)
new_zip.close()

This code will create a new ZIP file named new.zip that has the compressed contents of spam.txt.

# Keep in mind that, just as with writing to files, write mode will erase all existing contents of a ZIP file. If you want to simply add files to an existing ZIP file, pass 'a' as the second argument to zipfile.ZipFile() to open the ZIP file in append mode.

#-------------------- Step 1: Create a Regex for American-Style Dates
# The first part of the program will need to import the necessary modules and create a regex that can identify MM-DD-YYYY dates. The to-do comments will remind you what’s left to write in this program. Typing them as TODO makes them easy to find using Mu editor’s CTRL-F find feature. Make your code look like the following:


