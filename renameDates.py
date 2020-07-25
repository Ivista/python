#! python3
# renameDates.py - renames filenames with an American MM-DD-YY date format
# to European date format DD-MM-YY

import shutil
import os
import re

# create a regex that matches files with the american date format

date_Pattern = re.compile(r'''^(.*?) # all text before the date
    ((0|1)?\d)-     #One or two digits for the month
    ((0|1|2|3)\d)-  #One or two digits for the day
    ((19|20)\d\d)  #Four digits for the year
    (.*?)$          # all text after the date
    ''', re.VERBOSE)

# TODO: Loop over the files in the working directory. 
print(os.getcwd())

os.chdir('C:\\test')

print(os.getcwd())


for amer_Filename in os.listdir('.'):
    mo = date_Pattern.search(amer_Filename)

# TODO: Skip files without a date.   

    if mo == None:
        continue

# TODO: Get the different parts of the filename.   

    before_Part = mo.group(1)
    month_Part = mo.group(2)
    day_Part = mo.group(4)
    year_Part = mo.group(6)
    after_Part = mo.group(8)

#  TODO: Form the European-style filename.   

    euro_Filename = before_Part + day_Part + '-' + \
        month_Part + '-' + year_Part + after_Part

#  TODO: Get the full, absolute file paths.  

    abs_workingDirectory = os.path.abspath('.')
    amer_Filename = os.path.join(abs_workingDirectory, amer_Filename)
    euro_Filename = os.path.join(abs_workingDirectory, euro_Filename)


# TODO: Rename the files.

    print(f'Renameing "{amer_Filename}" to "{euro_Filename}"....')

    shutil.move(amer_Filename, euro_Filename)
