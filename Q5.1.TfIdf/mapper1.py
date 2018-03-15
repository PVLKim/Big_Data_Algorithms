#!/usr/bin/env python

import sys, os

stopwords = {'','i', 'me', 'my', 'myself', 'we', 'our', 'ours', 'ourselves', 'you', 'your', 'yours', 'yourself', 'yourselves',
             'he', 'him', 'his', 'himself', 'she', 'her', 'hers', 'herself', 'it', 'its', 'itself', 'they', 'them', 'their',
             'theirs', 'themselves', 'what', 'which', 'who', 'whom', 'this', 'that', 'these', 'those', 'am', 'is', 'are',
             'was', 'were', 'be', 'been', 'being', 'have', 'has', 'had', 'having', 'do', 'does', 'did', 'doing', 'a', 'an',
             'the', 'and', 'but', 'if', 'or', 'because', 'as', 'until', 'while', 'of', 'at', 'by', 'for', 'with', 'about',
             'against', 'between', 'into', 'through', 'during', 'before', 'after', 'above', 'below', 'to', 'from', 'up',
             'down', 'in', 'out', 'on', 'off', 'over', 'under', 'again', 'further', 'then', 'once', 'here', 'there', 'when',
             'where', 'why', 'how', 'all', 'any', 'both', 'each', 'few', 'more', 'most', 'other', 'some', 'such', 'no', 'nor',
             'not', 'only', 'own', 'same', 'so', 'than', 'too', 'very', 's', 't', 'can', 'will', 'just', 'don', 'should', 'now',
             '.', ',', '"', "'", '?', '!', ':', ';', '(', ')', '[', ']', '{', '}'}

# input comes from STDIN (standard input)
for line in sys.stdin:
    # extract document name
    filename = os.path.basename(os.environ["map_input_file"])
    # remove leading and trailing whitespace
    line = line.strip()
    # split the line into words
    words = line.split(' ')
    # remove secondary characters and lower the case
    for word in words:
        word = "".join(filter(str.isalpha, word)).lower()

        # removing stopwords
        if word in stopwords:
            continue
        key = word + ' ' + filename

        # write the results to STDOUT (standard output);
        print ('%s\t%s' % (key, 1))