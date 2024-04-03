import re


def valid_login(name):
    return re.findall("[^A-Za-z0-9_@-]{6,18}",name)


print(valid_login("my-p@ssw0rd"))