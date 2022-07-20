# You live in the city of Cartesia where all roads are laid out in a
# perfect grid. You arrived ten minutes too early to an appointment,
# so you decided to take the opportunity to go for a short walk.
# The city provides its citizens with a Walk Generating App on their
# phones -- everytime you press the button it sends you an array of one-letter
# strings representing directions to walk (eg. ['n', 's', 'w', 'e']).
# You always walk only a single block for each letter (direction) and you
# know it takes you one minute to traverse one city block, so create a function
# That will return true if the walk the app gives you will take you exactly ten
# minutes (you don't want to be early or late!) and will, of course, return you
# to your starting point. Return false otherwise.

# Note: you will always receive a valid array containing a
# random assortment of direction letters ('n', 's', 'e', or 'w' only).
# It will never give you an empty array (that's not a walk, that's standing
# still!).


def is_valid_walk(walk):
    # determine if walk is valid
    if len(walk) > 10:
        return False

    n = []
    s = []
    w = []
    e = []

    for direction in walk:
        if direction == 'n':
            n.append(direction)

        if direction == 's':
            s.append(direction)

        if direction == 'w':
            w.append(direction)

        if direction == 'e':
            e.append(direction)

    if len(n) != len(s) or len(w) != len(e):
        return False

    if len(walk) == 10:
        return True

    return False


def valid(char1, char2, list):
    return list.count(char1) == list.count(char2)


def is_valid_walk_02(walk):
    if (len(walk) == 10 and
        valid('n', 's', walk) and
            valid('e', 'w', walk)):
        return True

    return False


print(is_valid_walk(['e', 'w', 'n', 'w', 'w', 'e', 's', 'e', 'n', 's']))
print(is_valid_walk_02(['e', 'w', 'n', 'w', 'w', 'e', 's', 'e', 'n', 's']))
