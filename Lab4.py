import os
import filecmp
from pprint import pprint

myFile = open('mbox-short.txt', 'r')
fromLines = []

for element in myFile.readlines():
    if 'From' in element:
        fromLines.append(element)

name = ""
names = []
for statement in fromLines:
    name = statement.split()[1].split('@')[0]
    names.append(name)

pprint (names)
