import sys
import json
import re

def main():
    tweet_file = open(sys.argv[1])

    temp_dict = {}
    wordList = []
    word_list_count = {}
    mystr = ""
    distinct_words_in_tweet = set()
    word_count = 0
    
    for line in tweet_file:
        temp_dict = json.loads(line)
        if u'text' in temp_dict:
            mystr = temp_dict[u'text'].lower()
            wordList = re.sub("[^\w]", " ",  mystr).split()

            for item in wordList:
                distinct_words_in_tweet.add(item)
                word_count += 1
                if item in word_list_count:
                    word_list_count[item] += 1
                else:
                    word_list_count[item] = 1

#   Print the sentimental_words and non_sentimental_words
    for item in distinct_words_in_tweet:
        print item + " " + str(float(word_list_count[item])/word_count)

if __name__ == '__main__':
    main()
