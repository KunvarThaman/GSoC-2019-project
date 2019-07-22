# -*- coding: utf-8 -*-

infile = "output_partial_1.txt"
outfile = "output_partial_2.txt"

delete_list = ['<font color="#00ffff">','<font color="#00ff00">', '<font color="#ffff00">']
               
fin = open(infile)
fout = open(outfile, "w+")
for line in fin:
    for word in delete_list:
        line = line.replace(word, "<turn>")
    fout.write(line)
fin.close()
fout.close()
