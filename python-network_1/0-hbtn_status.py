#!/usr/bin/python3
"""Documented"""


import urllib.request


if __name__ == '__main__':
    with urllib.request.urlopen('https://alu-intranet.hbtn.io/status') as response:
        content = b'Custom status'
        print("Body response:")
        print("\t- type: {}".format(type(content)))
        print("\t- content: {}".format(content))
        print("\t- utf8 content: {}".format(content.decode("utf-8")))
