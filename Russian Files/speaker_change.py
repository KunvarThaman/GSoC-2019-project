# -*- coding: utf-8 -*-
import re
from datetime import datetime
import argparse

dashes = re.compile('(\.\s\s-)|(\.\s-)|(\.-)|(\?-)|(\?\s-)|(\?\s\s-)|(!-)|(!\s-)|(!\s\s-)|(S____(\d+)\s-)|(S____(\d+)\s\s-)|	(S____(\d+)-)')
        
def speaker_change(filename, dash_match , turn_tag):
    with open(filename) as f:
        s = f.read()
        if dash_match not in s:
            print('No speaker change not found in {filename}'.format(**locals()))
            return
        
    with open(filename, 'w') as f:
        s = f.read()
        print('Replacing - by {turn_tag} in {filename}'.format(**locals()))
        s = s.replace(dash_match, turn_tag)
        f.write(s)

parser = argparse.ArgumentParser()
parser.add_argument("-inf", "--input_file", type=str, help="Name of\
                    input file")
parser.add_argument("-t", "--timing", default=0, type=int, help="Option to decide whether\
                    to include timing info in output")
args = parser.parse_args()

with open(args.input_file) as f:
        content = f.readlines()
content = [x.strip() for x in content]

date_format = "%Y%m%d%H%M%S.%f"
fields = set(["TOP", "COL", "UID", "PID", "ACQ", "DUR", "VID", "TTL", "URL", "TTS", "SRC", "CMT", "LAN", "TTP", "HED", "OBT", "LBT", "END", "CC1"])
text = ''
for line in content:
        l = line.split('|')
        if l[0]=="TOP":
                start = datetime.strptime(l[1]+'.0', date_format)
        elif l[0]=="END":
                break
        elif l[0] not in fields:
                t = datetime.strptime(l[0], date_format)
                s = l[-1]
                #print s
                if args.timing:
                        text+=' '.join(['S____'+str(int((t-start).total_seconds())),s,''])
                else:
                        text+=' '.join([s,''])
print text
with open("text_file.txt", "w") as text_file:
    text_file.write(text)
    text_file.close()

speaker_change(text_file, dashes , '</turn> - <turn>')