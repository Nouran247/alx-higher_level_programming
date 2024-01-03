#!/usr/bin/python3
def uppercase(str):
    for i in range(str):
        if ord(i) >= 97 and ord(i) <= 122:
            i = char(ord(i) - 32)
            print("{:c}".format(i))
        else:
            print("{:c}".format(i), end="")
