# -*- coding: utf-8 -*-
import re

infile = "output_partial_2.txt"

outfile = "turn_tagged.txt"

reg_matches = re.findall(r'(\.\s\s-)|(\.\s-)|(\.-)|(\?-)|(\?\s-)|(\?\s\s-)|(!-)|(!\s-)|(!\s\s-)|(S____(\d+)\s-)|(S____(\d+)\s\s-)|	(S____(\d+)-)', open(infile).read(), re.I)
   
fin = open(infile)
fout = open(outfile, "w+")
for line in fin:
    for word in reg_matches:
        line = line.replace(word, "</turn> - <turn>")
    fout.write(line)
fin.close()
fout.close()
