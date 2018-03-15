#!/usr/bin/env python
import sys
words = []

for line in sys.stdin:
    word_doc, tf_idf = line.split('\t', 1)
    word, doc = word_doc.split(' ', 1)
    tf_idf = float(tf_idf)

    words.append([word, tf_idf])

top20 = sorted(words, key=lambda x: x[1], reverse=True)[:20]

for word, tfidf in top20:
    print('%s\t%s' % (word, tfidf))
