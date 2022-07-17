import re

# My solution


def add_binary(a, b):
    # your code here
    return re.sub(r'0b', '', bin(a+b))

# Solution made by someone else


def add_binary2(a, b):
    return f"{a + b:b}"


print(add_binary(1, 3123123123))
print(add_binary2(1, 3123123123))
