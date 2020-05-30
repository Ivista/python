import myCats
import shelve
import pprint
import os
from pathlib import Path

Path('spam') / 'bacon' / 'eggs'

print(str(Path('spam') / Path('bacon/eggs')))

homefolder = Path('c:/users/Al')

subfolder = Path('spam')

homefolder / subfolder

str(homefolder / subfolder)

Path.cwd()

Path(r'c:\users\bevan\spam').mkdir()


os.chdir('c:/test')

Path.home()

os.makedirs('c://delicious//walnut//waffels')

Path.cwd().is_absolute()

Path('bacon/spam/eggs').is_absolute()

Path('Pstestnew/scripts')

Path.home() / Path('PSTestnew/scripts')

os.path.abspath('.')

os.path.abspath('.//scripts')

os.path.isabs('.')

os.path.isabs(os.path.abspath('.'))

#---------------------------------------------------------------

from pathlib import Path
import os

p = Path('C:/Users/bevan/OneDrive/Documents')

for textFile in p.glob('*.???x'):
    print(textFile)

#------------------------------------------------------
list(p.glob('*.docx'))
#-----------------------------------------------------
# Listing files and doing something with them if they are a file or directory. 

p = Path('C:/Users/bevan/OneDrive/Documents')
myList = []
nameList =[]
dirList = []
for textFile in p.glob('*'):
    if textFile.is_file(): #Check if file, if so do somthing. 
        myList.append(textFile)
        nameList.append(textFile.name)
    if textFile.is_dir():  #Check if directory, if so do something
        dirList.append(textFile.name)

    #print(textFile)

q = Path('C:/Users/bevan/OneDrive/Documents')

#--------------------------------------------------------------------------
# Checking Path Validity
# Many Python functions will crash with an error if you supply them with a path that does not exist. Luckily, Path objects have methods to check whether a given path exists and whether it is a file or folder. Assuming that a variable p holds a Path object, you could expect the following:

# Calling p.exists() returns True if the path exists or returns False if it doesn’t exist.
# Calling p.is_file() returns True if the path exists and is a file, or returns False otherwise.
# Calling p.is_dir() returns True if the path exists and is a directory, or returns False otherwise.
# On my computer, here’s what I get when I try these methods in the interactive shell:

winDir = Path('C:/Windows')

notExistsDir = Path('C:/This/Folder/Does/Not/Exist')

calcFile = Path('C:/Windows/System32/calc.exe')

winDir.exists()

winDir.is_dir()

notExistsDir.exists()

calcFile.is_file()

calcFile.is_dir()

#Reading and writing from a File Object---------------------------------------

# Since every different type of binary file must be handled in its own way, this book will not go into reading and writing raw binary files directly. Fortunately, many modules make working with binary files easier—you will explore one of them, the shelve module, later in this chapter. The pathlib module’s read_text() method returns a string of the full contents of a text file. Its write_text() method creates a new text file(or overwrites an existing one) with the string passed to it. Enter the following into the interactive shell:

prom pathlib import Path

p = Path('spam.txt')

p.write_text('hello world')

p.read_text()

Path.home()

# Opening Files with the open() Function
# To open a file with the open() function, you pass it a string path indicating the file you want to open
# it can be either an absolute or relative path. The open() function returns a File object.

# Try it by creating a text file named hello.txt using Notepad or TextEdit. Type Hello, world! as the content of this text file and save it in your user home folder. Then enter the following into the interactive shell:


helloFile = open(Path.home() / 'hello.txt')

print(helloFile)
helloFile

# Opening Files with the open() Function
# To open a file with the open() function, you pass it a string path indicating the file you want to open
# it can be either an absolute or relative path. The open() function returns a File object.

# Try it by creating a text file named hello.txt using Notepad or TextEdit. Type Hello, world! as the content of this text file and save it in your user home folder. Then enter the following into the interactive shell:

helloFile = open(Path.home() / 'hello.txt')


# The call to open() returns a File object. A File object represents a file on your computer
# it is simply another type of value in Python, much like the lists and dictionaries you’re already familiar with. In the previous example, you stored the File object in the variable helloFile. Now, whenever you want to read from or write to the file, you can do so by calling methods on the File object in helloFile.

# Reading the Contents of Files
# Now that you have a File object, you can start reading from it. If you want to read the entire contents of a file as a string value, use the File object’s read() method. Let’s continue with the hello.txt File object you stored in helloFile. Enter the following into the interactive shell:helloContent = helloFile.read()

helloContent = helloFile.read()
helloContent

# Alternatively, you can use the readlines() method to get a list of string values from the file, one string for each line of text. For example, create a file named sonnet29.txt in the same directory as hello.txt and write the following text in it:

sonnetFile = open(Path.home() / 'sonnet29.txt')

sonnetFile.readlines()

# Note that, except for the last line of the file, each of the string values ends with a newline character \n. A list of strings is often easier to work with than a single large string value.

#-------------------------------------------------------------------------

# Writing to FilesPython allows you to write content to a file in a way similar to how the print() function “writes” strings to the screen. You can’t write to a file you’ve opened in read mode, though. Instead, you need to open it in “write plaintext” mode or “append plaintext” mode, or write mode and append mode for short.Write mode will overwrite the existing file and start from scratch, just like when you overwrite a variable’s value with a new value. Pass 'w' as the second argument to open() to open the file in write mode. Append mode, on the other hand, will append text to the end of the existing file. You can think of this as appending to a list in a variable, rather than overwriting the variable altogether. Pass 'a' as the second argument to open() to open the file in append mode.If the filename passed to open() does not exist, both write and append mode will create a new, blank file. After reading or writing a file, call the close() method before opening the file again.Let’s put these concepts together. Enter the following into the interactive shell:


baconFile = open('bacon1.txt', 'w')
baconFile.write('Hello World!\n')

baconFile.close()
baconFile = open('bacon1.txt', 'a')
baconFile.write('Bacon is not a vegetable!')

baconFile.close()
baconFile = open('bacon1.txt', 'r')
content = baconFile.read()
baconFile.close()
content

# First, we open bacon.txt in write mode. Since there isn’t a bacon.txt yet, Python creates one. Calling write() on the opened file and passing write() the string argument 'Hello, world! /n' writes the string to the file and returns the number of characters written, including the newline. Then we close the file.To add text to the existing contents of the file instead of replacing the string we just wrote, we open the file in append mode. We write 'Bacon is not a vegetable.' to the file and close it. Finally, to print the file contents to the screen, we open the file in its default read mode, call read(), store the resulting File object in content, close the file, and print content.Note that the write() method does not automatically add a newline character to the end of the string like the print() function does. You will have to add this character yourself.As of Python 3.6, you can also pass a Path object to the open() function instead of a string for the filename.

#---------------------------------------------------------------------------------------------------------------------------------------

# SAVING VARIABLES WITH THE SHELVE MODULE
# You can save variables in your Python programs to binary shelf files using the shelve module. This way, your program can restore data to variables from the hard drive. The shelve module will let you add Save and Open features to your program. For example, if you ran a program and entered some configuration settings, you could save those settings to a shelf file and then have the program load them the next time it is run.


shelfFile = shelve.open('mydata')
cats = ['Zophie', 'Pooka', 'Sam', 'Suki', 'Patience']
shelfFile['cats'] = cats
shelfFile.close()

# To read and write data using the shelve module, you first import shelve. Call shelve.open() and pass it a filename, and then store the returned shelf value in a variable. You can make changes to the shelf value as if it were a dictionary. When you’re done, call close() on the shelf value. Here, our shelf value is stored in shelfFile. We create a list cats and write shelfFile['cats'] = cats to store the list in shelfFile as a value associated with the key 'cats' (like in a dictionary). Then we call close() on shelfFile. Note that as of Python 3.7, you have to pass the open() shelf method filenames as strings. You can’t pass it Path object.After running the previous code on Windows, you will see three new files in the current working directory: mydata.bak, mydata.dat, and mydata.dir. On macOS, only a single mydata.db file will be created.These binary files contain the data you stored in your shelf. The format of these binary files is not important
# you only need to know what the shelve module does, not how it does it. The module frees you from worrying about how to store your program’s data to a file.Your programs can use the shelve module to later reopen and retrieve the data from these shelf files. Shelf values don’t have to be opened in read or write mode—they can do both once opened. Enter the following into the interactive shell:

shelfFile = shelve.open('mydata')

type(shelfFile)

shelfFile['cats']

shelfFile.close()

# Here, we open the shelf files to check that our data was stored correctly. Entering shelfFile['cats'] returns the same list that we stored earlier, so we know that the list is correctly stored, and we call close().Just like dictionaries, shelf values have keys() and values() methods that will return list-like values of the keys and values in the shelf. Since these methods return list-like values instead of true lists, you should pass them to the list() function to get them in list form. Enter the following into the interactive shell:

shelfFile = shelve.open('mydata')
list(shelfFile.keys())
list(shelfFile.values())

# Here, we open the shelf files to check that our data was stored correctly. Entering shelfFile['cats'] returns the same list that we stored earlier, so we know that the list is correctly stored, and we call close().Just like dictionaries, shelf values have keys() and values() methods that will return list-like values of the keys and values in the shelf. Since these methods return list-like values instead of true lists, you should pass them to the list() function to get them in list form. Enter the following into the interactive shell:

# Plaintext is useful for creating files that you’ll read in a text editor such as Notepad or TextEdit, but if you want to save data from your Python programs, use the shelve module.

#----------------------------------------------------------------------------------------

#------------------------------------------------------------------------------------------------
# Saving Variables with the pprint.pformat()
# FunctionRecall from “Pretty Printing” on page 118 that the pprint.pprint() function will “pretty print” the contents of a list or dictionary to the screen, while the pprint.pformat() function will return this same text as a string instead of printing it. Not only is this string formatted to be easy to read, but it is also syntactically correct Python code. Say you have a dictionary stored in a variable and you want to save this variable and its contents for future use. Using pprint.pformat() will give you a string that you can write to a .py file. This file will be your very own module that you can import whenever you want to use the variable stored in it.For example, enter the following into the interactive shell:

# import pprint
# cats = [{'name': 'Zophie', 'desc': 'chubby'}, {'name': 'Pooka', 'desc': 'fluffy',}]
# pprint.pformat(cats)

# fileObj = open('myCats.py', 'w')
# fileObj.write('cats = ' + pprint.pformat(cats) + '\n')
# fileObj.close()

cats = [{'name': 'Zophie', 'desc': 'chubby'},
        {'name': 'Pooka', 'desc': 'fluffy'}]
pprint.pformat(cats)
fileObj = open('myCats.py', 'w')
fileObj.write('cats = ' + pprint.pformat(cats) + '\n')
fileObj.close()


# Here, we import pprint to let us use pprint.pformat(). We have a list of dictionaries, stored in a variable cats. To keep the list in cats available even after we close the shell, we use pprint.pformat() to return it as a string. Once we have the data in cats as a string, it’s easy to write the string to a file, which we’ll call myCats.py.The modules that an import statement imports are themselves just Python scripts. When the string from pprint.pformat() is saved to a .py file, the file is a module that can be imported just like any other.And since Python scripts are themselves just text files with the .py file extension, your Python programs can even generate other Python programs. You can then import these files into scripts.

print(myCats.cats)

myCats.cats[0]
myCats.cats[0]['name']

# The benefit of creating a .py file(as opposed to saving variables with the shelve module) is that because it is a text file, the contents of the file can be read and modified by anyone with a simple text editor. For most applications, however, saving data using the shelve module is the preferred way to save variables to a file. Only basic data types such as integers, floats, strings, lists, and dictionaries can be written to a file as simple text. File objects, for example, cannot be encoded as text.

#