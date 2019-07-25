# -*- coding: utf-8 -*-

infile = "output_final_2.txt"
outfile = "output_final_3.txt"

delete_list = ['? -','?-']

fin = open(infile)
fout = open(outfile, "w+")
for line in fin:
    for word in delete_list:
        line = line.replace(word, "? </turn> - <turn>")
    fout.write(line)
fin.close()
fout.close()

