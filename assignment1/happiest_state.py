import sys
import json
import re
import collections

def main():
    states = {
        'AK': 'Alaska',
        'AL': 'Alabama',
        'AR': 'Arkansas',
        'AS': 'American Samoa',
        'AZ': 'Arizona',
        'CA': 'California',
        'CO': 'Colorado',
        'CT': 'Connecticut',
        'DC': 'District of Columbia',
        'DE': 'Delaware',
        'FL': 'Florida',
        'GA': 'Georgia',
        'GU': 'Guam',
        'HI': 'Hawaii',
        'IA': 'Iowa',
        'ID': 'Idaho',
        'IL': 'Illinois',
        'IN': 'Indiana',
        'KS': 'Kansas',
        'KY': 'Kentucky',
        'LA': 'Louisiana',
        'MA': 'Massachusetts',
        'MD': 'Maryland',
        'ME': 'Maine',
        'MI': 'Michigan',
        'MN': 'Minnesota',
        'MO': 'Missouri',
        'MP': 'Northern Mariana Islands',
        'MS': 'Mississippi',
        'MT': 'Montana',
        'NA': 'National',
        'NC': 'North Carolina',
        'ND': 'North Dakota',
        'NE': 'Nebraska',
        'NH': 'New Hampshire',
        'NJ': 'New Jersey',
        'NM': 'New Mexico',
        'NV': 'Nevada',
        'NY': 'New York',
        'OH': 'Ohio',
        'OK': 'Oklahoma',
        'OR': 'Oregon',
        'PA': 'Pennsylvania',
        'PR': 'Puerto Rico',
        'RI': 'Rhode Island',
        'SC': 'South Carolina',
        'SD': 'South Dakota',
        'TN': 'Tennessee',
        'TX': 'Texas',
        'UT': 'Utah',
        'VA': 'Virginia',
        'VI': 'Virgin Islands',
        'VT': 'Vermont',
        'WA': 'Washington',
        'WI': 'Wisconsin',
        'WV': 'West Virginia',
        'WY': 'Wyoming'
    }

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
        tweet_dict = json.loads(line)
        if u'text' in tweet_dict:
            mystr = tweet_dict[u'text'].lower()
            wordList = re.sub("[^\w]", " ",  mystr).split()
            count = 0
            for item in wordList:
                if item.encode("utf-8") in scores.keys():
                    count += scores[item]

            #Only if we find any sentiment value in the tweet will we investigate the geocode
            if count > 0:
                # Using the coordinates field inside place
                # Just a place holder, cannot refer coordinates database
                # to find the state
##                if u'geo' in tweet_dict and tweet_dict[u'geo'] is not None:
##                    print tweet_dict[u'geo']
                full_name = []
                # Examples of full_name under place field in tweet: "Washington, DC" "Sandhurst" "Pretoria" "Bristol" "Texas, USA"
                if u'place' in tweet_dict and tweet_dict[u'place'] is not None:
                    full_name = re.sub("[^\w]", " ", tweet_dict[u'place'][u'full_name']).split()
                    for item in full_name:
                        # The item can be the key or the value. Like Texas above
                        if item in states:
                            increment(item)
##                            if happiest_state[item] is not None:
##                                happiest_state[item] = happiest_state[item] + 1
##                            else:
##                                happiest_state[item] = 1
                        elif item in states.values():
                            for k,v in states.iteritems():
                                if v == item:
                                    increment(k)

    top = collections.Counter(happiest_state)
    for k,v in top.most_common(1):
        print k
        #sys.stdout.write(k + " " + str(v))
        
        
happiest_state = {}
def increment(state_code):
    if state_code in happiest_state:
        happiest_state[state_code] += 1
    else:
        happiest_state[state_code] = 1

if __name__ == '__main__':
    main()
