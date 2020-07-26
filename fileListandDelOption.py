import os
from pathlib import Path
import send2trash
path_search = 'C:\\Users\\bevan\\Downloads'

for fol_der, sub_folder, file_names in os.walk(path_search):

    for file_name in file_names:

        file_location = os.path.join(os.path.abspath(fol_der), file_name)
        file_size = round(os.path.getsize(
            os.path.join(fol_der, file_name)) / (1024*1024))

        if file_size >= 100:
            print(f'{file_location} {file_size} MB ')
            deleteFile_yesno = input(
                'Enter Y if you would like to send to trash, or hit any other key ')
            if deleteFile_yesno == 'Y':
                send2trash.send2trash(file_location)

        # print(os.path.join(os.path.abspath(fol_der), file_name) + ' MB ', end='')
        # print(round(os.path.getsize(os.path.join(fol_der, file_name)) / (1024*1024)))
