# -*- coding: utf-8 -*-

infile = "output_messy.txt"
outfile = "output_clean.txt"

delete_list = ['</font>']
               
fin = open(infile)
fout = open(outfile, "w+")
for line in fin:
    for word in delete_list:
        line = line.replace(word, "</turn>")
    fout.write(line)
fin.close()
fout.close()
