Search for all the files containing <font> :

$grep -iRl “<font” ./

Output these file names into another text file for cleaner results and better readability:

$grep -iRl “<font” ./ > files_with_font_tag.txt

We run the preprocess.py on the sample files:

python preprocess.py -inf <input-file-name> -t <0 or 1>
Where -t [ 1 or 0] can be used to toggle the relative time occurrence of each block of words.

For example: 

python preprocess.py -inf 2018-07-13_0730_ES_Antena-3_El_hormiguero.txt -t 0 > output.txt
 
We want to determine which words form the starting of a sentence. Hence we would look for the words following a stop-punctuation mark, such as . or ! or ?. However, when we look at output_messy.txt, we can see that there are <font> tags to indicate the speaker change, sometimes at the beginning of a new line such as :

<font color="#00ff00">que pueden matizar posiciones.</font> <font color="#00ff00">Pero hay que recordar</font> <font color="#00ff00">las verdades del barquero.

They’re going to interfere when we are collecting the words which are at the beginning of the sentence for the frequency list. 
So, we create a new output file output_clean.txt which removes all the font tags as we don’t need them for the frequency list and important information isn’t lost.

There weren’t a lot of different font colors being used, so I manually searched for them and created a list as:

delete_list = ['</font>','<font color="#00ffff">','<font color="#00ff00">', '<font color="#ffff00">']

Now, we just open the files as infile and outfile:

fin = open(infile)
fout = open(outfile, "w+")

We go line by line in the infile and see if any of the words from delete_list occur. If it does, we replace it with whitespace in the outfile.


for line in fin:
    for word in delete_list:
        line = line.replace(word, "")
    fout.write(line)

Now, we're done and close the files: 

fin.close()
fout.close()

Looking at the output_clean.txt, we can see that there are no instances of font tags occurring now. We now apply the code for finding the first words of each sentence and create a frequency list.
