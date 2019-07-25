# -*- coding: utf-8 -*-
import re, os
from collections import Counter
import argparse

parser = argparse.ArgumentParser()
parser.add_argument("-inf", "--input_file", type=str, help="Name of\input file")
args = parser.parse_args()


reg_matches = re.compile(r'\(.*?\)')

with open(args.input_file, 'r') as rf, open('freq_round.txt', 'a') as wf:
    content = rf.read()
    matches = reg_matches.findall(content)
    for match in matches:
        wf.write(match + '\n')
        
with open('freq_round.txt') as f:
    wordcount = Counter(f.read().split())
    print(wordcount)
