def __create_dict_from_file(file_name):
    d = dict()
    with open(file_name, 'r') as file:
        for name in file:
            name = name[:len(name) - 1]
            if name in d:
                d[name] += 1
            else:
                d[name] = 1

    return d


def __create_top_from_dict(d):
    l = list(d.keys())
    l.sort(key=lambda x: d[x], reverse=True)
    return l[:10]


def make_top():
    d = __create_dict_from_file("server/database/name_frequency.txt")
    top = __create_top_from_dict(d)

    return top
