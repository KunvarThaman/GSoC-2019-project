# -*- coding: utf-8 -*-

# split up a paragraph into sentences using regex

def splitParagraphIntoSentences(paragraph):
    ''' break a paragraph into sentences
        and return a list '''
    import re
    sentenceEnds = re.compile('[.!?]')
    sentenceList = sentenceEnds.split(paragraph)
    return sentenceList

if __name__ == '__main__':
	with open(args.input_file) as f:
        content = f.readlines()
	content = [x.strip() for x in content]
    sentences = splitParagraphIntoSentences(content)
    for s in sentences:
        print s.strip()

'''
#Check later
text = ''.join(open(args.input_file).readlines())
sentences = re.split(r' *[\.\?!][\'"\)\]]* *', text)
'''