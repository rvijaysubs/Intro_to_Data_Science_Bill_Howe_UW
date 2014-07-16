import sys
import json
import re

def hw():
    print 'Hello, world!'

def lines(fp):
    print str(len(fp.readlines()))

def main():
    afinnfile = open(sys.argv[1])
    tweet_file = open(sys.argv[2])
    scores = {} # initialize an empty dictionary
    for line in afinnfile:
        term, score  = line.split("\t")  # The file is tab-delimited. "\t" means "tab character"
        scores[term] = int(score)  # Convert the score to an integer.

    temp_dict = {}
    wordList = []
    mystr = ""
    
    for line in tweet_file:
        temp_dict = json.loads(line)
        if u'text' in temp_dict:
            mystr = temp_dict[u'text'].lower()
            wordList = re.sub("[^\w]", " ",  mystr).split()
            count = 0
            for item in wordList:
                if item.encode("utf-8") in scores.keys():
                    count += scores[item]
            print count
        else:
            print 0

if __name__ == '__main__':
    main()
