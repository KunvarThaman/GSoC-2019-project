Since the readability in the text file is quite low, we create a csv file for the same.

First, we need to import the csv library:

import csv

Now we open the frequency list we got in the previous step:

#EDIT: Change this with the args.

with open('testfile.txt', 'r') as in_file:
       stripped = (line.strip() for line in in_file)
       lines = (line.split(",") for line in stripped if line)
       
Now, we write the file into csv format:
       wiith open('testing.csv', 'w') as out_file:
       writer = csv.writer(out_file)
       writer.writerow(('title', 'intro'))
       writer.writerows(lines)
       
I got all the frequencies in different tabs, however, all in one row, separated by columns, instead of the other way around. I dug around a bit to find out the reason and it is that csv doesn't support that is because variable-length lines are not really supported on most filesystems. 
