# Your goal in this kata is to implement a difference function,
# which subtracts one list from another and returns the result.

# It should remove all values from list a, which are present
# in list b keeping their order.

# array_diff([1,2],[1]) == [2]


def array_diff(a, b):
    # your code here
    copy_array_a = a.copy()

    for item in a:
        if item in b:
            copy_array_a.remove(item)

    return copy_array_a


# Code of another person

def array_diff_another_person(a, b):
    return [x for x in a if x not in b]


print(array_diff([1, 2, 2], [2]))
print(array_diff_another_person([1, 2, 2], [2]))
