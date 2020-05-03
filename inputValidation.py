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

# #---------------------------------------------------
# The allowRegexes and blockRegexes Keyword Arguments
# You can also use regular expressions to specify whether an input is allowed or not. The allowRegexes and blockRegexes keyword arguments take a list of regular expression strings to determine what the PyInputPlus function will accept or reject as valid input. For example, enter the following code into the interactive shell so that inputNum() will accept Roman numerals in addition to the usual numbers:


responce = pyip.inputNum(allowRegexes=[r'(I|V|X|L|C|D|M)+', r'zero'])

print(responce)

#--------------------------------------------------------------------------
# You can also specify a list of regular expression strings that a PyInputPlus function won’t accept by using the blockRegexes keyword argument. Enter the following into the interactive shell so that inputNum() won’t accept even numbers:

responce = pyip.inputNum(blockRegexes=[r'[02468]'])

#-----------------------------------------------------
# Passing a Custom Validation Function to inputCustom()
# You can write a function to perform your own custom validation logic by passing the function to inputCustom(). For example, say you want the user to enter a series of digits that adds up to 10. There is no pyinputplus.inputAddsUpToTen() function, but you can create your own function that:
# Accepts a single string argument of what the user entered
# Raises an exception if the string fails validation
# Returns None (or has no return statement) if inputCustom() should return the string unchanged
# Returns a non-None value if inputCustom() should return a different string from the one the user entered
# Is passed as the first argument to inputCustom()
# For example, we can create our own addsUpToTen() function, and then pass it to inputCustom(). Note that the function call looks like inputCustom(addsUpToTen) and not inputCustom(addsUpToTen()) because we are passing the addsUpToTen() function itself to inputCustom(), not calling addsUpToTen() and passing its return value.

#see the for loop which changes string digits in a list into integer values in the same list
#this one is worth noting for the future.


def addsUpToTen(numbers):
    numberslist = list(numbers)
    for i, digit in enumerate(numberslist):
        numberslist[i] = int(digit)
    if sum(numberslist) != 10:
        raise Exception('The digits must add up to 10, not %s. ' %
                        (sum(numberslist)))
    return int(numbers)


responce = pyip.inputCustom(addsUpToTen)
#---------------------------------------------------------------------------
