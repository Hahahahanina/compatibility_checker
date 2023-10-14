__MAX = 100


def __calculate_index(name):
    h = 0
    for symbol in name:
        h *= ord(symbol)
        h += ord(symbol) * 3
        h %= __MAX
    return h


def __calculate_common_index(index1, index2):
    index = (index1 * 7 + index2 * 7 + min(index1, index2) * 5 + max(index1, index2) * 3) % __MAX
    return index


def calculate_compatibility(name1, name2):
    index1 = __calculate_index(name1)
    index2 = __calculate_index(name2)

    index = __calculate_common_index(index1, index2)

    return index
