#!/usr/bin/env python
import sys

current_word = None
word_doc = []
count_wpd = []
docs_pw = 0
word = None

# input comes from STDIN
for line in sys.stdin:
    line = line.strip()
    # parse the input we got from mapper.py
    word, doc_count_wpd = line.split('\t', 1)
    doc, count, wpd = doc_count_wpd.split(' ', 2)

    if current_word == word:
        docs_pw += 1
        word_doc.append(word + ' ' + doc)
        count_wpd.append(count + ' ' + wpd)

    else:
        if current_word:
            for i in range(len(word_doc)):
                value = count_wpd[i] + ' ' + str(docs_pw)
                print('%s\t%s' % (word_doc[i], value))
        current_word = word
        word_doc = [word + ' ' + doc]
        count_wpd = [count + ' ' + wpd]
        docs_pw = 1
        
if current_word == word:
    for i in range(len(word_doc)):
        value = count_wpd[i] + ' ' + str(docs_pw)
        print('%s\t%s' % (word_doc[i], value))