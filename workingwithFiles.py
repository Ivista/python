my_file = open('movies.txt', 'a')
my_file.write('Highlander, there can be only one\n')
my_file.write('Jaws, derda\n')
my_file.close()

my_file = open('movies.txt', 'r')
data = my_file.read()
my_file.close()
print(data)

for line in open('movies.txt'):
    print(line, end="")

import openpyxl

wb = openpyxl.load_workbook('example.xlsx')

sheet = wb['Sheet1']
print(sheet['A1'])

print(sheet['A1'].value)

c = sheet['B1']
print(c.value)

print('Row %s is %s' % (c.coordinate, c.value))

print(sheet['C1'].value)

print(sheet['A1'].value)

#--------------------------------------------------------

print(sheet.cell(row=1, column=2).value)

for i in range(1,8):
    print(i, sheet.cell(row=i, column=2).value)

#---------------------------------------------------------

print(sheet.max_row) 

print(sheet.max_column)

#-----------------------------------------------------

from openpyxl.utils import get_column_letter, column_index_from_string

print(get_column_letter(1))
print(get_column_letter(2))
print(get_column_letter(27))
print(get_column_letter(900))

print(get_column_letter(sheet.max_column))

print(column_index_from_string('A'))

print(column_index_from_string('AA'))

# #----------------------------------------------------------------------------
# Getting Rows and Columns from the SheetsYou can slice Worksheet objects to get all the Cell objects in a row, column, or rectangular area of the spreadsheet. Then you can loop over all the cells in the slice. Enter the following into the interactive shell:


wb = openpyxl.load_workbook('example.xlsx')

print(wb)

sheet = wb['Sheet1']

print(list(sheet['A1':'C3']))

for rowOfCellObjects in sheet['A1':'C3']:
    for cellObj in rowOfCellObjects:
        print(cellObj.coordinate, cellObj.value)
    print('------End Of Row------')
