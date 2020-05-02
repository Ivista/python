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



# #----------------------------------------------------------------
# The blank Keyword Argument
# By default, blank input isn’t allowed unless the blank keyword argument is set to True:

responce = pyip.inputNum('Enter Num: ')
print(responce)

responce = pyip.inputNum('Enter Num: ', blank=True)
print(responce)

# Use blank = True if you’d like to make input optional so that the user doesn’t need to enter anything.

#-----------------------------------------------------------------------

# The limit, timeout, and default Keyword Arguments
# By default, the PyInputPlus functions will continue to ask the user for valid input forever(or for as long as the program runs). If you’d like a function to stop asking the user for input after a certain number of tries or a certain amount of time, you can use the limit and timeout keyword arguments. Pass an integer for the limit keyword argument to determine how many attempts a PyInputPlus function will make to receive valid input before giving up, and pass an integer for the timeout keyword argument to determine how many seconds the user has to enter valid input before the PyInputPlus function gives up.

# If the user fails to enter valid input, these keyword arguments will cause the function to raise a RetryLimitException or TimeoutException, respectively. For example, enter the following into the interactive shell:

responce = pyip.inputNum(limit=3)

responce = pyip.inputNum('Enter num in 10 seconds', timeout=10)

print(responce)

# When you use these keyword arguments and also pass a default keyword argument, the function returns the default value instead of raising an exception. Enter the following into the interactive shell:

responce = pyip.inputNum('Enter a Number: ', limit=2, default='N/A')
print(responce)
