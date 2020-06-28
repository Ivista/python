from pathlib import Path

p = []

p.append(Path('C:/users/43301380/Desktop'))

p.append(Path('C:/Users/43301380/Downloads'))

# p.glob('*')

# print(p.glob('*'))

# print(list(p.glob('*.txt')))

# print(list(p.glob('*.?x?')))

for i in p:
        
        for textFilePathObj in i.glob('*clarity*'):
                print(textFilePathObj)


print('hello')