#----------------------------------------------------
# An example manual code input checker. 

import pyinputplus as pyip
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
#----------------------------------------------------------
# Pyinputplus is testing for the input of a number


responce = pyip.inputNum()

print(responce)

#-----------------------------------------------------------
# Just as you can pass a string to input() to provide a prompt, you can pass a string to a PyInputPlus function’s prompt keyword argument to display a prompt:

responce = input('Enter a Number')

responce = pyip.inputInt(prompt='Enter a Number!')

print(responce)

help(pyip.inputChoice)
