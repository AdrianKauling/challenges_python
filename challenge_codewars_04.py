def tower_builder(n_floors):
    # build here

    if n_floors == 0:
        return []

    initial_num_of_asterisk = 1
    pyramid = []
    asterisk_amount_in_base = n_floors * 2 - 1

    for n in range(n_floors):
        pyramid.append('*'*initial_num_of_asterisk)
        initial_num_of_asterisk += 2

        while len(pyramid[n]) != asterisk_amount_in_base:
            pyramid[n] = " "+pyramid[n]+" "
        # print(len(pyramid[n]))

    return pyramid


# Code of Other person

def tower_builder_other_person(n_floors):
    # build here

    if n_floors == 0:
        return []

    pyramid = []

    for n in range(1, n_floors+1):
        # pyramid.append('*'*initial_num_of_the_asterisk)
        # initial_num_of_the_asterisk += 2

        # while len(pyramid[n]) != asterisk_amount_in_base:
        #     pyramid[n] = " "+pyramid[n]+" "
        # print(len(pyramid[n]))
        # print(n)
        asterisk = '*' * (2 * n - 1)
        space = ' ' * (n_floors - n)
        pyramid.append(space + asterisk + space)

    return pyramid


print(tower_builder(6))
print(tower_builder_other_person(6))
