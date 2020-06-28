import os

totalsize = 0

for filename in os.listdir('C:\\ProgramData\\Scalable Software\\Asset Vision Agent'):
        totalsize += os.path.getsize(os.path.join('C:\\ProgramData\\Scalable Software\\Asset Vision Agent', filename))
        filesze = os.path.getsize(os.path.join('C:\\ProgramData\\Scalable Software\\Asset Vision Agent', filename))
        print(filename, filesze)

print(totalsize)

