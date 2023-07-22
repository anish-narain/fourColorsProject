import csv
import string

counter = 0
word_to_search = 'Herschel'
with open('page-content.csv', encoding='UTF-8') as f:
    for line in csv.reader(f):
        s = str(line)
        no_punc = s.translate(str.maketrans('','', string.punctuation))
        if any(word_to_search in l for l in map(str.lower, no_punc)):
            counter = counter + 1
        print(no_punc)
        print(counter)

''' The functionality I need is something that will go through my csv file, for each line return the number of times a word has occurred
Then there will be a queue of 5 items. If the number of times is one of the top 5 add it to the queue (and remove the bottom most value)
Add special priority to questions
Return top 5
'''

