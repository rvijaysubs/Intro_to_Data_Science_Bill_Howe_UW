import sys
import json
import collections

def main():
    tweet_file = open(sys.argv[1])

    temp_dict1 = {}
    temp_list1 = []
    hash_tags = {}
    mystr = ""
    
    for line in tweet_file:
        temp_dict1 = json.loads(line)
        if u'entities' in temp_dict1 and u'hashtags' in temp_dict1[u'entities']:
            temp_list1 = temp_dict1[u'entities'][u'hashtags']
            for i in temp_list1:
                mystr = i[u'text'].encode("ascii", errors='ignore')         
                if len(mystr) > 0:
                    if mystr in hash_tags:
                        hash_tags[mystr] += 1
                    else:
                        hash_tags[mystr] = 1

    top10 = collections.Counter(hash_tags)
    for k,v in top10.most_common(10):
        print k + " " + str(v)

if __name__ == '__main__':
    main()
