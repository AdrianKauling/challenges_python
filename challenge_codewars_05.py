# You will be given an array of numbers. You have to sort the
# odd numbers in ascending order while leaving the even numbers
# at their original positions.


def sort_array(source_array):
    # Return a sorted array.
    def filter_numbers_odd(num):
        if num % 2 != 0:
            return True
        else:
            return False

    odds = list(filter(filter_numbers_odd, source_array))
    odds.sort()

    count_lenght_list_odds = 0
    for i in range(len(source_array)):
        if source_array[i] % 2 != 0:
            source_array[i] = odds[count_lenght_list_odds]
            count_lenght_list_odds += 1
    return source_array


list1 = [9, 8, 7, 6, 5, 4, 3, 2, 1, 0]
print(sort_array(list1))
