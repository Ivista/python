import re
def isPhoneNumber(text):
    if len(text) != 12:
        return False
    for i in range(0, 3):
        if not text[i].isdecimal():
            return False
    if text[3] != "-":
        return False
    for i in range(4, 7):
        if not text[i].isdecimal():
            return False
    if text[7] != "-":
        return False
    for i in range(8, 12):
        if not text[i].isdecimal():
            return False
    return True

#print("Is 415-555-4242 a phone number?")
#print(isPhoneNumber("415-555-4242"))
#print('Is Moshi moshi a phone number?')
#print(isPhoneNumber('Moshi moshi'))


message = 'Call me at 415-555-1011 tomorrow. 415-555-9999 is my office.'
for i in range(len(message)):
    chunk = message[i:i+12]
    if isPhoneNumber(chunk):
        print('Phone number found: ' + chunk)
print('Done')


phoneNumRegEx = re.compile(r'\d\d\d-\d\d\d-\d\d\d\d')
mo = phoneNumRegEx.search('My number is 415-555-4242.')
print('phone num found: ' + mo.group())

# The mo variable name is just a generic name to use for Match objects. This example might seem complicated at first, but it is much shorter than the earlier isPhoneNumber.py program and does the same thing.

# Here, we pass our desired pattern to re.compile() and store the resulting Regex object in phoneNumRegex. Then we call search() on phoneNumRegex and pass search() the string we want to match for during the search. The result of the search gets stored in the variable mo. In this example, we know that our pattern will be found in the string, so we know that a Match object will be returned. Knowing that mo contains a Match object and not the null value None, we can call group() on mo to return the match. Writing mo.group() inside our print() function call displays the whole match, 415-555-4242.

#-----------------------------------------------------------------------------

# Grouping with Parentheses
# Say you want to separate the area code from the rest of the phone number. Adding parentheses will create groups in the regex: (\d\d\d)-(\d\d\d -\d\d\d\d). Then you can use the group() match object method to grab the matching text from just one group.

# The first set of parentheses in a regex string will be group 1. The second set will be group 2. By passing the integer 1 or 2 to the group() match object method, you can grab different parts of the matched text. Passing 0 or nothing to the group() method will return the entire matched text. Enter the following into the interactive shell:


phoneNumRegEx = re.compile(r'(\d\d\d)-(\d\d\d-\d\d\d\d)')
mo = phoneNumRegEx.search('My phone is 415-555-4242')
print(mo.group(1))
print(mo.group(2))
print(mo.group(0))
print(mo.group())

areaCode, mainNumber = mo.groups()
print(areaCode)
print(mainNumber)


#---------------------------------------------------------------------------------
# Parentheses have a special meaning in regular expressions, but what do you do if you need to match a parenthesis in your text? For instance, maybe the phone numbers you are trying to match have the area code set in parentheses. In this case, you need to escape the(and) characters with a backslash. Enter the following into the interactive shell:

phoneNumRegEx = re.compile(r'(\(\d\d\d\)) (\d\d\d-\d\d\d\d)')
mo = phoneNumRegEx.search('My phone number is (415) 555-4242.')
print(mo.group(1))
print(mo.group(2))


#---------------------------------------------------------------------------------
# Matching Multiple Groups with the Pipe
# The | character is called a pipe. You can use it anywhere you want to match one of many expressions. For example, the regular expression r'Batman|Tina Fey' will match either 'Batman' or 'Tina Fey'.

# When both Batman and Tina Fey occur in the searched string, the first occurrence of matching text will be returned as the Match object. Enter the following into the interactive shell:


heroRegex = re.compile(r'Batman|Tina Fey')
mo1 = heroRegex.search('Batman and Tina Fey')
mo1.group()

print(mo1.group())

mo2 = heroRegex.search("Tina Fey and Batman")
print(mo2.group())

#----------------------------------------------------------------------
# You can also use the pipe to match one of several patterns as part of your regex. For example, say you wanted to match any of the strings 'Batman', 'Batmobile', 'Batcopter', and 'Batbat'. Since all these strings start with Bat, it would be nice if you could specify that prefix only once. This can be done with parentheses. Enter the following into the interactive shell:


batRegex = re.compile(r'Bat(man|mobile|copter|bat)')
mo = batRegex.search('Batmobile lost a wheel')
print(mo.group())
print(mo.group(1))

#-----------------------------------------------------------------------

# Optional Matching with the Question Mark
# Sometimes there is a pattern that you want to match only optionally. That is, the regex should find a match regardless of whether that bit of text is there. The ? character flags the group that precedes it as an optional part of the pattern. For example, enter the following into the interactive shell:

batRegex = re.compile(r'Bat(wo)?man')
mo1 = batRegex.search('The adventures of Batman')
print(mo1.group())

mo2 = batRegex.search('The adventures of Batwoman')
print(mo2.group())

# The(wo)? part of the regular expression means that the pattern wo is an optional group. The regex will match text that has zero instances or one instance of wo in it. This is why the regex matches both 'Batwoman' and 'Batman'.

#----------------------------------------------------------------------


phoneRegex = re.compile(r'(\d\d\d-)?\d\d\d-\d\d\d\d')
mo1 = phoneRegex.search('My phone number is 415-555-4242')
print(mo1.group())

mo2 = phoneRegex.search('My phone number is 555-4242')
print(mo2.group())

# Using the earlier phone number example, you can make the regex look for phone numbers that do or do not have an area code. Enter the following into the interactive shell:


phoneRegex = re.compile(r'(\d\d\d-)?\d\d\d-\d\d\d\d')
mo1 = phoneRegex.search('My phone number is 415-555-4242')
print(mo1.group())

mo2 = phoneRegex.search('My phone number is 555-4242')
print(mo2.group())

# You can think of the ? as saying, “Match zero or one of the group preceding this question mark.”If you need to match an actual question mark character, escape it with \?.


#-------------------------------------------------------------------

# Matching Zero or More with the Star
# The * (called the star or asterisk) means “match zero or more”—the group that precedes the star can occur any number of times in the text. It can be completely absent or repeated over and over again. Let’s look at the Batman example again.


batRegex = re.compile(r'Bat(wo)*man')
mo1 = batRegex.search('The Adventures of Batman')
print(mo1.group())

mo2 = batRegex.search('The Adventures of Batwoman')
print(mo2.group())

mo3 = batRegex.search('The Adventures of Batwowowowoman')
print(mo3.group())

# For 'Batman', the(wo) * part of the regex matches zero instances of wo in the string
# for 'Batwoman', the(wo) * matches one instance of wo
# and for 'Batwowowowoman', (wo) * matches four instances of wo.If you need to match an actual star character, prefix the star in the regular expression with a backslash, \*.

#-------------------------------------------------------------

# Matching One or More with the Plus
# While * means “match zero or more, ” the + (or plus) means “match one or more.” Unlike the star, which does not require its group to appear in the matched string, the group preceding a plus must appear at least once. It is not optional. Enter the following into the interactive shell, and compare it with the star regexes in the previous section:


batRegex = re.compile(r'Bat(wo)+man')
mo1 = batRegex.search('The Adventures of Batwoman')

print(mo1.group())

mo2 = batRegex.search('The Adventures of Batwowowowoman')
print(mo2.group())

mo3 = batRegex.search('The Adventures of Batman')
print(mo3 == None)

# The regex Bat(wo)+man will not match the string 'The Adventures of Batman', because at least one wo is required by the plus sign.If you need to match an actual plus sign character, prefix the plus sign with a backslash to escape it: \+.

#----------------------------------------------------------
# Matching Specific Repetitions with Braces
# If you have a group that you want to repeat a specific number of times, follow the group in your regex with a number in braces. For example, the regex(Ha){3} will match the string 'HaHaHa', but it will not match 'HaHa', since the latter has only two repeats of the(Ha) group.

# Instead of one number, you can specify a range by writing a minimum, a comma, and a maximum in between the braces. For example, the regex(Ha){3, 5} will match 'HaHaHa', 'HaHaHaHa', and 'HaHaHaHaHa'.

# You can also leave out the first or second number in the braces to leave the minimum or maximum unbounded. For example, (Ha){3, } will match three or more instances of the(Ha) group, while (Ha){, 5} will match zero to five instances. Braces can help make your regular expressions shorter.

haRegex = re.compile(r'(Ha){3}')
mo1 = haRegex.search('HaHaHa')
print(mo1.group())

mo2 = haRegex.search('Ha')
print(mo2 == None)

#----------------------------------------------------------
# Since(Ha){3, 5} can match three, four, or five instances of Ha in the string 'HaHaHaHaHa', you may wonder why the Match object’s call to group() in the previous brace example returns 'HaHaHaHaHa' instead of the shorter possibilities. After all, 'HaHaHa' and 'HaHaHaHa' are also valid matches of the regular expression(Ha){3, 5}.

# Python’s regular expressions are greedy by default, which means that in ambiguous situations they will match the longest string possible. The non-greedy(also called lazy) version of the braces, which matches the shortest string possible, has the closing brace followed by a question mark.

# Enter the following into the interactive shell, and notice the difference between the greedy and non-greedy forms of the braces searching the same string:

greedyHaRegex = re.compile(r'(Ha){3,5}')
mo1 = greedyHaRegex.search('HaHaHaHaHa')
print(mo1.group())

nonGreedyRegex = re.compile(r'(Ha){3,5}?')
mo2 = nonGreedyRegex.search('HaHaHaHaHa')
print(mo2.group())

# Note that the question mark can have two meanings in regular expressions: declaring a non-greedy match or flagging an optional group. These meanings are entirely unrelated.

# #------------------------------------------------------------
# In addition to the search() method, Regex objects also have a findall() method. While search() will return a Match object of the first matched text in the searched string, the findall() method will return the strings of every match in the searched string. To see how search() returns a Match object only on the first instance of matching text, enter the following into the interactive shell:

phoneRegex = re.compile(r'\d\d\d-\d\d\d-\d\d\d\d')
mo = phoneRegex.search('Cell: 415-555-9999 Work: 212-555-0000')
print(mo.group())

# On the other hand, findall() will not return a Match object but a list of strings—as long as there are no groups in the regular expression. Each string in the list is a piece of the searched text that matched the regular expression. Enter the following into the interactive shell:
phoneNumRegex = re.compile(r'\d\d\d-\d\d\d-\d\d\d\d')  # Has no groups!
print(phoneNumRegex.findall('Cell: 415-555-9999 Work: 212-555-0000'))

phoneNumRegex = re.compile(r'(\d\d\d)-(\d\d\d)-(\d\d\d\d)')  # Has groups
mo1 = phoneNumRegex.findall('Cell: 415-555-9999 Work: 212-555-0000')

print(mo1[1])

#---------------------------------------------------------------------  
# CHARACTER CLASSES
# In the earlier phone number regex example, you learned that \d could stand for any numeric digit. That is, \d is shorthand for the regular expression(0 | 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8 | 9). There are many such shorthand character classes, as shown in Table 7-1.

xmasRegex = re.compile(r'\d+\s\w+')
print(xmasRegex.findall('12 drummers, 11 pipers, 10 lords, 9 ladies, 8 maids, 7 swans, 6 geese, 5 rings, 4 birds, 3 hens, 2 doves, 1 partridge, r mongooses'))

# The regular expression \d +\s\w + will match text that has one or more numeric digits(\d+), followed by a whitespace character(\s), followed by one or more letter/digit/underscore characters(\w+). The findall() method returns all matching strings of the regex pattern in a list.

# MAKING YOUR OWN CHARACTER CLASSES
# There are times when you want to match a set of characters but the shorthand character classes(\d, \w, \s, and so on) are too broad. You can define your own character class using square brackets. For example, the character class [aeiouAEIOU] will match any vowel, both lowercase and uppercase. Enter the following into the interactive shell

vowelRegex = re.compile(r'[aeiouAEIOU]')
print(vowelRegex.findall('RoboCop eats baby food. BABY FOOD.'))

# You can also include ranges of letters or numbers by using a hyphen. For example, the character class [a-zA-Z0-9] will match all lowercase letters, uppercase letters, and numbers.

# Note that inside the square brackets, the normal regular expression symbols are not interpreted as such. This means you do not need to escape the ., *, ?, or () characters with a preceding backslash. For example, the character class [0-5.] will match digits 0 to 5 and a period. You do not need to write it as [0-5\.].

# By placing a caret character ( ^ ) just after the character class’s opening bracket, you can make a negative character class. A negative character class will match all the characters that are not in the character class. For example, enter the following into the interactive shell:

consonantRegex = re.compile(r'[^aeiouAEIOU]')
print(consonantRegex.findall('RoboCop eats baby food. BABY FOOD.'))

# The Caret and Dollar Sign CharactersYou can also use the caret symbol ( ^ ) at the start of a regex to indicate that a match must occur at the beginning of the searched text. Likewise, you can put a dollar sign ($) at the end of the regex to indicate the string must end with this regex pattern. And you can use the ^ and $ together to indicate that the entire string must match the regex—that is, it’s not enough for a match to be made on some subset of the string.For example, the r'^Hello' regular expression string matches strings that begin with 'Hello'. Enter the following into the interactive shell:

beginsWithHello = re.compile(r'^Hello')
mo = beginsWithHello.search('Hello world!')
print(beginsWithHello.search('Hello world!'))

mo2 = beginsWithHello.search('He said hello.')
print(beginsWithHello.search('He said hello.') == None)

# The r'\d$' regular expression string matches strings that end with a numeric character from 0 to 9. Enter the following into the interactive shell:

endsWithNumber = re.compile(r'\d$')
print(endsWithNumber.search('Your number is 42'))
print(endsWithNumber.search('Your number is forty two'))

# The r'^\d+$' regular expression string matches strings that both begin and end with one or more numeric characters. Enter the following into the interactive shell:

wholeStringIsNum = re.compile(r'^\d+$')
print(wholeStringIsNum.search('1234567890'))
print(wholeStringIsNum.search('12345xyz67890') == None)
print(wholeStringIsNum.search('12  34567890') == None)

# The last two search() calls in the previous interactive shell example demonstrate how the entire string must match the regex if ^ and $ are used.

# I always confuse the meanings of these two symbols, so I use the mnemonic “Carrots cost dollars” to remind myself that the caret comes first and the dollar sign comes last.

# THE WILDCARD CHARACTER
# The . (or dot) character in a regular expression is called a wildcard and will match any character except for a newline. For example, enter the following into the interactive shell:

atRegex = re.compile(r'..at')
print(atRegex.findall('The cat in the hat sat on the flat mat'))

#------------------------------------------------------------------------


#----------------------------------------------------------------

# Matching Everything with Dot-StarSometimes you will want to match everything and anything. For example, say you want to match the string 'First Name:', followed by any and all text, followed by 'Last Name:', and then followed by anything again. You can use the dot-star(.*) to stand in for that “anything.” Remember that the dot character means “any single character except the newline, ” and the star character means “zero or more of the preceding character.”

nameRegex = re.compile(r'First Name: (.*) Last Name: (.*)')
mo = nameRegex.search('First Name: Albaba genie Last Name: Sweigart')

print(mo.group(1))
print(mo.group(2))
print('Hello world')

# The dot-star uses greedy mode: It will always try to match as much text as possible. To match any and all text in a non-greedy fashion, use the dot, star, and question mark(.*?). Like with braces, the question mark tells Python to match in a non-greedy way.

# Enter the following into the interactive shell to see the difference between the greedy and non-greedy versions:

nongreedRegex = re.compile(r'<.*?>')
mo = nongreedRegex.search('<To serve man> for dinner.>')
print(mo.group())

greedyRex = re.compile(r'<.*>')
mo = greedyRex.search('<To serve man> for dinner.>')
print(mo.group())

# Both regexes roughly translate to “Match an opening angle bracket, followed by anything, followed by a closing angle bracket.” But the string '<To serve man> for dinner.>' has two possible matches for the closing angle bracket. In the non-greedy version of the regex, Python matches the shortest possible string: '<To serve man>'. In the greedy version, Python matches the longest possible string: '<To serve man> for dinner.>'.

#-----------------------------------------------------------------------------------

# Matching Newlines with the Dot Character
# The dot-star will match everything except a newline. By passing re.DOTALL as the second argument to re.compile(), you can make the dot character match all characters, including the newline character.

noNewlineRegex = re.compile('.*')
print(noNewlineRegex.search(
    'Serve the public trust.\nProtect teh innocent.\nUphold the law.').group())

newlineRegex = re.compile('.*', re.DOTALL)
print(newlineRegex.search(
    'Serve the public trust.\nProtect the innocent. \nUphold the law.').group())

# The regex noNewlineRegex, which did not have re.DOTALL passed to the re.compile() call that created it, will match everything only up to the first newline character, whereas newlineRegex, which did have re.DOTALL passed to re.compile(), matches everything. This is why the newlineRegex.search() call matches the full string, including its newline characters.

#-------------------------------------------------------
# CASE-INSENSITIVE MATCHING
# Normally, regular expressions match text with the exact casing you specify. For example, the following regexes match completely different strings:

# >> > regex1 = re.compile('RoboCop')
# >> > regex2 = re.compile('ROBOCOP')
# >> > regex3 = re.compile('robOcop')
# >> > regex4 = re.compile('RobocOp')

# But sometimes you care only about matching the letters without worrying whether they’re uppercase or lowercase. To make your regex case-insensitive, you can pass re.IGNORECASE or re.I as a second argument to re.compile(). Enter the following into the interactive shell:

roboCop = re.compile(r'robocop', re.I)
print(roboCop.search('Robocop is part man, part machine, all cop.').group())
print(roboCop.search('ROBOCOP protects the innocent').group())

print(roboCop.search(
    'AL why does your programming bood talk about robocop so much.').group())

# SUBSTITUTING STRINGS WITH THE SUB() METHOD
# Regular expressions can not only find text patterns but can also substitute new text in place of those patterns. The sub() method for Regex objects is passed two arguments. The first argument is a string to replace any matches. The second is the string for the regular expression. The sub() method returns a string with the substitutions applied.

# For example, enter the following into the interactive shell:

namesRegex = re.compile(r'Agent \w+')
print(namesRegex.sub('CENSORED', 'Agent Alice gave the secret documents to Agent Bob.'))

# Sometimes you may need to use the matched text itself as part of the substitution. In the first argument to sub(), you can type \1, \2, \3, and so on, to mean “Enter the text of group 1, 2, 3, and so on, in the substitution.”

# For example, say you want to censor the names of the secret agents by showing just the first letters of their names. To do this, you could use the regex Agent(\w)\w * and pass r'\1****' as the first argument to sub(). The \1 in that string will be replaced by whatever text was matched by group 1—that is, the(\w) group of the regular expression.


agentNamesRegex = re.compile(r'Agent (\w)\w*')
mo4 = agentNamesRegex.sub(
    r'\1****', 'Agent Alice told Agent Carol that Agent Eve knew Agent Bob was a double agent.')
print(mo4.group(1))

#----------------------------------------------------------------------------------


namesRegex = re.compile(r'Agent \w*\s\w+')
print(namesRegex.sub('CENSORED', 'Agent Alice gave the secret documents to Agent Bob.'))

# MANAGING COMPLEX REGEXES
# Regular expressions are fine if the text pattern you need to match is simple. But matching complicated text patterns might require long, convoluted regular expressions. You can mitigate this by telling the re.compile() function to ignore whitespace and comments inside the regular expression string. This “verbose mode” can be enabled by passing the variable re.VERBOSE as the second argument to re.compile().

# Now instead of a hard-to-read regular expression like this:

phoneRegex = re.compile(r'((\d{3} |\(\d{3}\))?(\s | - |\.)?\d{3}(\s | - |\.)\d{4}(\s*(ext | x | ext.)\s *\d{2, 5})?)')

# you can spread the regular expression over multiple lines with comments like this:

phoneRegex = re.compile(r'''(
    (\d{3}|\(\d{3}\))?            # area code
    (\s|-|\.)?                    # separator
    \d{3}                         # first 3 digits
    (\s|-|\.)                     # separator
    \d{4}                         # last 4 digits
    (\s*(ext|x|ext.)\s*\d{2,5})?  # extension
    )''', re.VERBOSE)

# Note how the previous example uses the triple-quote syntax(''') to create a multiline string so that you can spread the regular expression definition over many lines, making it much more legible.

# # symbol and everything after it to the end of the line are ignored. Also, the extra spaces inside the multiline string for the regular expression are not considered part of the text pattern to be matched. This lets you organize the regular expression so it’s easier to read.
# The comment rules inside the regular expression string are the same as regular Python code: the

#-------------------------------------------------------------------------------
import re
robocop = re.compile(r'\s*\d\d\d\s+(ext|xten|x)?\s+(\(\s*d\w+\))')

print(robocop.search('    456   x  (   dj)').group(2))


#https: // globalnewswire.systems.uk.hsbc

robocop = re.compile(
    r'(http:|https:)+\/\/\w+\.systems\.(\w{2,12})\.([a-zA-Z]{2,4})')

print(robocop.search('https://globalnewswire.systems.uk.hsbc').group(2))


#------------------------------------------------------
# Written code to search through a string with a RegEx to find dates.  Then check that the dates have valid numbers in them 
# for days months and years, also prints out successs for failure!


import re


def monthanddayCheck(mon, dy):

    while True:

        if mon in ['04', '06', '09', '11'] and int(dy) > 30:
            #if int(dy) >30:
            print('This month does not have more than 30 days!')
            return False
        elif mon in ['01', '03', '04', '05', '07', '08', '10', '12'] and int(dy) > 31:
            print('This month does not have more then 31 days')
            return False
        elif mon in ['02'] and int(dy) > 29:
            print('This months does not have more than 29 days!')
            return False
        elif mon not in ['01', '03', '04', '05', '07', '08', '10', '12', '02', '04', '06', '09', '11', '12']:
            print('This month does not exist!')
            return False
        else:
            return True


dateCheck = re.compile(r'([0-3]\d)\/([0-3]\d)\/([1-2]\d\d\d)')

mo = dateCheck.findall('07/06/2004 Work 34/09/2011')

for modate in mo:
    print(f"{modate[0]}\\{modate[1]}\\{modate[2]}")
    day = modate[0]
    month = modate[1]
    year = modate[2]

    result = monthanddayCheck(month, day)

    if result == False:
        print('Date is not correct!')
    else:
        print('Date checks out!')

print('End of date examination')

#--------------------------------------------------------------------------

