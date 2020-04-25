#-------------------------------------------------
import re


def matchAndStrip(alph, cts):  # Function

    # if extra argument passed, then strip charecters passed in second argument from string.
    if cts and alph:
        # Any charecter not present in the set []
        stringStrip = re.compile(r'[^\s]+')

    # If just string argument passed then strip whitespace with a regex
    elif cts:
        # if extra argument passed, then strip charecters passed in second argument from string.
alpha = ''
rata = 'dave'

matchAndStrip(alpha, rata)
