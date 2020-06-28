import os
import openpyxl

wb = openpyxl.Workbook()

sheetNew =wb.active

totalsize = 0

path = 'C:\\Program Files\\Scalable Software'

files = []
refile = []


for r, d, f in os.walk(path):
        for file in f:
                files.append(os.path.join(r, file))

for cnt, filename in enumerate(files):
        totalsize += os.path.getsize(filename)
        filesze = os.path.getsize(filename)
        refile.append([])
        refile[cnt].append(filename, filesze)
        #refile[cnt].append(filesze)
        print(filename, filesze)

for cnt1, lisref in enumerate(refile):
        print(cnt1)
        for d, measure in enumerate(lisref):
                print(d, measure)

                sheetNew.cell(column=d+1, row=cnt1+1).value = measure
wb.save('ScalableProgFiles.xlsx')


# for i, (k, v) in enumerate(refile.items()):
#     print(i, k, v)
print(totalsize)