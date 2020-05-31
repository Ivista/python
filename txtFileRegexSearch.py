from pathlib import Path

# TODO: open all *.txt files in a directory 

p = Path('C:/test')

for testFileObject in p.glob('*.txt'):
    print(testFileObject)


# TODO: Search through each line in  txt file for a user supplied regex expression

# TODO: print output to the screen

