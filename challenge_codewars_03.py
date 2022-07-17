# Description
#
# Write a function, persistence, that takes in a positive parameter num and
# returns its multiplicative persistence, which is the number of times you
# must multiply the digits in num until you reach a single digit.


def persistence(num):
    # your code
    product = 1
    persistence = 0
    while num > 9:
        for position in range(len(str(num))):
            product *= int(str(num)[position])
        num = product
        persistence += 1
        product = 1
    return persistence


print(persistence(4))
