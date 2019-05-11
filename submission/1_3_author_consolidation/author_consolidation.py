#!/usr/bin/env python3
import sys

authors = {}

for line in sys.stdin:
    name, mail = line.rstrip().split(';')
    try:
        authors[name].add(mail)
    except KeyError:
        authors[name] = set()
        authors[name].add(mail)


for name in sorted(authors.keys(), key=lambda n: n.lower()):
    print('{0} {1}'.format(name, ' '.join(authors[name])))
