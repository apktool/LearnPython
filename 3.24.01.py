# yaml demo

from yaml import load, dump
from yaml import Loader, Dumper

stream = open('example.yaml', 'r')

data = load(stream, Loader=Loader)
print(data)

print('-----------')

output = dump(data, Dumper=Dumper)
print(output)


# example.yaml
'''
a: 1
b:
    c: 3
    d: 4
'''
