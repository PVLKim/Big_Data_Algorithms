#!/usr/bin/env python

import sys

# input comes from STDIN
for line in sys.stdin:
    line = line.strip()
    word_doc, count_wpd = line.split('\t', 1)
    word, doc = word_doc.split(' ', 1)
    value = doc + ' ' + count_wpd

    print('%s\t%s' % (word, value))

