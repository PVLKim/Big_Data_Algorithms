#!/usr/bin/env python
import sys

current_doc = None
words_per_doc = 0
word_counts = []
words = []
doc = ""

# input comes from STDIN
for line in sys.stdin:
    line = line.strip()
    # parse the input we got from mapper.py
    doc, word_count = line.split('\t', 1)
    word, count = word_count.split(' ', 1)
    count = int(count)

    if current_doc == doc:
        words_per_doc += count
        word_counts.append(count)
        words.append(word + ' ' + doc)

    else:
        if current_doc:
            for w_count in range(len(words)):
                value = str(word_counts[w_count]) + ' ' + str(words_per_doc)
                print('%s\t%s' % (words[w_count], value))
        current_doc = doc
        words_per_doc = 0
        word_counts = []
        words = []


if current_doc == doc:
    for w_count in range(len(words)):
        value = str(word_counts[w_count]) + ' ' + str(words_per_doc)
        print('%s\t%s' % (words[w_count], value))


