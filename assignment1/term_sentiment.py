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
    non_sentimental_words = {}
    sentimental_words_in_tweet = set()
    
    for line in tweet_file:
        temp_dict = json.loads(line)
        if u'text' in temp_dict:
            mystr = temp_dict[u'text'].lower()
            wordList = re.sub("[^\w]", " ",  mystr).split()

            count = 0
            non_sentimental_words_in_tweet = set()
            for item in wordList:
                if item.encode("utf-8") in scores.keys():
                    count += scores[item]
                    sentimental_words_in_tweet.add(item)
                else:
                    non_sentimental_words_in_tweet.add(item)

            for item in non_sentimental_words_in_tweet:
                if item in non_sentimental_words:
                    non_sentimental_words[item]["count"] = non_sentimental_words[item]["count"] + count
                    non_sentimental_words[item]["total_count"] = non_sentimental_words[item]["total_count"] + 1
                else:
                    non_sentimental_words[item] = {}
                    non_sentimental_words[item]["count"] = count
                    non_sentimental_words[item]["total_count"] = 1

#   Print the sentimental_words and non_sentimental_words
    for item in sentimental_words_in_tweet:
        print item + " " + str(scores[item])

    for item in non_sentimental_words:
        print item + " " + str(float(non_sentimental_words[item]["count"])/non_sentimental_words[item]["total_count"])

if __name__ == '__main__':
    main()
