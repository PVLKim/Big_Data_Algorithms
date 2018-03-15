#!/usr/bin/env python
import sys

for line in sys.stdin:
    line = line.strip()
    word_doc, count = line.split('\t', 1)
    word, doc = word_doc.split(' ', 1)

    print ('%s\t%s' % (doc, word + ' ' + count))