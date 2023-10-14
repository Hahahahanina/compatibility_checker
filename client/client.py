import requests
from lxml import etree
from io import StringIO


address = 'http://127.0.0.1:5000/'


def parse_compatibility(html):
    parser = etree.HTMLParser()
    tree = etree.parse(StringIO(html), parser)
    phrase = tree.xpath('/html/body/div')[0].text
    return phrase


def parse_top(html):
    parser = etree.HTMLParser()
    tree = etree.parse(StringIO(html), parser)
    l = []
    l.append(tree.xpath('/html/body/h1')[0].text)
    for i in range(10):
        l.append(tree.xpath('/html/body/div')[i].text)
    return '\n'.join(l)


def get_stat():
    html = requests.get(address + 'get_statistics').text
    print(parse_top(html))


def check(name1, name2):
    resp = requests.post(address + 'enter_names', data={'name1': name1, 'name2': name2})
    html = requests.get(address + 'checker').text
    print(parse_compatibility(html))


while True:
    print("Choose mod")
    print("Get statistics: get")
    print("Check compatibility: check")
    print("Exit: exit")

    command = str(input())
    print()

    if command == "get":
        get_stat()
    elif command == "check":
        print("Enter the first name:")
        name1 = str(input())
        print("Enter the second name:")
        name2 = str(input())
        check(name1, name2)
    elif command == "exit":
        break
    else:
        print("This command doesn't exist")

    print()
