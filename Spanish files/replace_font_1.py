# -*- coding: utf-8 -*-
#There has been an unsolved error when the replace_font_1,2, 3 are merged into one file. Until that is resolved, they're kept separate.

infile = "output_messy.txt"
outfile = "output_partial_!.txt"

delete_list = ['</font>']
               
fin = open(infile)
fout = open(outfile, "w+")
for line in fin:
    for word in delete_list:
        line = line.replace(word, "</turn>")
    fout.write(line)
fin.close()
fout.close()
