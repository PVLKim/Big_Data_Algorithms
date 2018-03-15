#!/usr/bin/env python
import sys
from math import log10

unique_docs = set()
wd = []
c_wpd_docpw = []

# input comes from STDIN
for line in sys.stdin:
    line = line.strip()
    word_doc, count_wpd_docpw = line.split('\t', 1)
    word, doc = word_doc.split(' ', 1)
    count, wpd, docpw = count_wpd_docpw.split(' ', 2)
    c_wpd_docpw.append([float(count), float(wpd), float(docpw)])
    wd.append(word_doc)

    if doc not in unique_docs:
        unique_docs.add(doc)

total_docs = len(unique_docs)
lst = [list(x) for x in zip(*c_wpd_docpw)]
word_count, words_per_doc, docs_per_word = lst[0], lst[1], lst[2]

if len(wd) != len(word_count):
    pass
else:
    for i in range(len(wd)):
        print('%s\t%s' % (wd[i], (word_count[i] / words_per_doc[i]) * log10(2.0 * total_docs / docs_per_word[i])))






