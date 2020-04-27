#-------------------------------------------------
import re


def matchAndStrip(alph, cts):  # Function
    global strngres

    # if extra argument passed, then strip charecters passed in second argument from string.
    if cts and alph:
        # Any charecter not present in the set []
        stringStrip = re.compile(r'[^\s]+')
        stringresults = stringStrip.search(cts)
        strngres = stringresults.group()
        for letter in alph:
            strngres = strngres.replace(letter, '')
            print(strngres)

    # If just string argument passed then strip whitespace with a regex
    elif cts:
        stringStrip = re.compile(r'[^\s]+')
        stringresults = stringStrip.search(cts)
        strngres = stringresults.group()
        
        print('hello')


# alpha = 'ea'
# rata = '  dave  '
strngres = ''

alpha = input('Input charecters to be striped and enter it here:')
rata = input('Enter string which will have whitspace charecters stripped:')


matchAndStrip(alpha, rata)

print(strngres)

