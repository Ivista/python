#----------------------------------------------------
# An example manual code input checker. 

while True:
    print('Enter your age:')
    age = input()
    try:
        age = int(age)
    except:
        print('Please use numeric digits')
        continue
    if age < 1:
        print('Please enter a positeve number.')
        continue
    break
print(f'Your age is {age}')

#--------------------------------------------------------------
import pyinputplus
