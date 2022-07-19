# Given n, take the sum of the digits of n.
# If that value has more than one digit, continue reducing in
# this way until a single-digit number is produced. The input will
# be a non-negative integer.


def digital_root(n):

    if n < 0:
        return

    while len(str(n)) != 1:
        value_tmp = 0
        for str_num in str(n):
            value_tmp += int(str_num)
        n = value_tmp

    return n


print(digital_root(16))
print(digital_root(942))
print(digital_root(132189))
print(digital_root(493193))
