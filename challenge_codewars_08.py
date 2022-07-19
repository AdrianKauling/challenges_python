# Given two arrays a and b write a function comp(a, b)
# (or compSame(a, b)) that checks whether the two arrays have the "same"
# elements, with the same multiplicities (the multiplicity
# of a member is the number of times it appears). "Same" means, here,
# that the elements in b are the elements in a squared, regardless of
# the order.


def comp(array1, array2):
    # your code
    for item_array_1 in array1:
        is_has = array2.count(item_array_1 ** 2)

        if is_has != 0:
            array2.remove(item_array_1 ** 2)
        else:
            return False
    return True


# Code of another person


# def comp_another_person(array1, array2):
#     try:
#         return sorted([i ** 2 for i in array1]) == sorted(array2)
#     except:
#         return False


a = [121, 144, 19, 161, 19, 144, 19, 11]
b = [121, 14641, 20736, 361, 25921, 361, 20736, 361]

c = [121, 144, 19, 161, 19, 144, 19, 11]
d = [11*11, 121*121, 144*144, 19*19, 161*161, 19*19, 144*144, 19*19]

e = [121, 144, 19, 161, 19, 144, 19, 11]
f = [132, 14641, 20736, 361, 25921, 361, 20736, 361]

g = [121, 144, 19, 161, 19, 144, 19, 11]
h = [121, 14641, 20736, 36100, 25921, 361, 20736, 361]

# print(aa.count(3))
# print(b)
# b.remove(361)
# print(b)

print(comp(a, b))
print(comp(c, d))
print(comp(e, f))
print(comp(g, h))
