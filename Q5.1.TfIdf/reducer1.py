#!/usr/bin/env python
import sys

current_word_doc = None
current_count = 0
word_doc = None

# input comes from STDIN
for line in sys.stdin:
    line = line.strip()
    # parse the input we got from mapper.py
    word_doc, count = line.split('\t', 1)

    # convert count (currently a string) to int
    count = int(count)


    # this IF-switch only works because Hadoop sorts map output
    # by key (here: word) before it is passed to the reducer
    if current_word_doc == word_doc:
        current_count += count
    else:
        if current_word_doc:
            # write result to STDOUT
            print ('%s\t%s' % (current_word_doc, current_count))
        current_count = count
        current_word_doc = word_doc

# do not forget to output the last word if needed!
if current_word_doc == word_doc:
    print ('%s\t%s' % (current_word_doc, current_count))

