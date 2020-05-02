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

#-----------------------------------------------------------------------------------------------

# The inputNum(), inputInt(), and inputFloat() functions, which accept int and float numbers, also have min, max, greaterThan, and lessThan keyword arguments for specifying a range of valid values. For example, enter the following into the interactive shell:


responce = pyip.inputNum('Enter num: ', min=4)

print(responce)

responce = pyip.inputNum('Enter num: ', greaterThan=4)

print(responce)

responce = pyip.inputNum('Enter num: ', min=4, lessThan=6)

print(responce)



#----------------------------------------------------------------

# The inputNum(), inputInt(), and inputFloat() functions, which accept int and float numbers, also have min, max, greaterThan, and lessThan keyword arguments for specifying a range of valid values. For example, enter the following into the interactive shell:

responce = pyip.inputNum('Enter Num: ')
print(responce)

responce = pyip.inputNum('Enter Num: ', blank=True)
print(responce)

# Use blank = True if you’d like to make input optional so that the user doesn’t need to enter anything.
