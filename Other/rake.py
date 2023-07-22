import csv
from rake_nltk import Rake
rake = Rake()

def readFile(fileName): #reads file and gets rid of punctuation
    a = ""
    with open(fileName, encoding='UTF-8') as f:
        for line in csv.reader(f):
            s = str(line)
            #no_punc = s.translate(str.maketrans('','', string.punctuation))
            #print(s)
            a = a + s
    
    return a

doc = readFile('p2.csv')

rake.extract_keywords_from_text(doc)

print(rake.get_ranked_phrases_with_scores())
# [(4.0, 'deep learning'), (1.0, 'useful'), (1.0, 'subfield'), (1.0, 'ai')]