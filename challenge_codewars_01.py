import re

# My solution


def disemvowel(string):
    return re.sub(r'a|e|i|o|u|A|E|I|O|U', '', string)


# Solution made by someone else

def disemvowel2(string):
    return re.sub('[aeiou]', '', string, flags=re.IGNORECASE)


print(disemvowel('adrIan'))
print(disemvowel2('adRiAn'))
