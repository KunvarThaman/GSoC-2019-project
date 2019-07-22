In the collections module, there is a very useful object to calculate the frequency of words, called Counter.

from collections import Counter

It's basically a dictionary that is specialized to count the instances of key-value in an iterable. 

with open('output_clean.txt') as f1,open('freq_start.txt','w') as f2:
    wordcount = Counter(f1.read().split())
    print(wordcount)
