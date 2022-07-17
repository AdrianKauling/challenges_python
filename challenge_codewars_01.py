# Description

# Trolls are attacking your comment section!

# A common way to deal with this situation is to remove all of the vowels from
# the trolls' comments, neutralizing the threat.

# Your task is to write a function that takes a string and return a new string
# with all vowels removed.

# For example, the string "This website is for losers LOL!" would become "Ths
# wbst s fr lsrs LL!".

# Note: for this kata y isn't considered a vowel.


import re

# My solution


def disemvowel(string):
    return re.sub(r'a|e|i|o|u|A|E|I|O|U', '', string)


# Solution made by someone else

def disemvowel2(string):
    return re.sub('[aeiou]', '', string, flags=re.IGNORECASE)


print(disemvowel('adrIan'))
print(disemvowel2('adRiAn'))
