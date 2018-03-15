#!/usr/bin/env python
import sys

for line in sys.stdin:
    line = line.strip()
    wd, tfidf = line.split('\t', 1)
    print('%s\t%s' % (wd, tfidf))
