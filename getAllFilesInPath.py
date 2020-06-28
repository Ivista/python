import os

#path = 'C:\\ProgramData\\Scalable Software\\'
path = 'C:\\GitRepo\\'

files = []

for r, d, f in os.walk(path):
        for file in f:
                files.append(os.path.join(r, file))

for f in files:
        print(f)






print('hello')