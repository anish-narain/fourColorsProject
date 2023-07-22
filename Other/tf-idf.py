import csv
import string

#1. Import packages: we need to tokenize to create word token, itemgetter to sort the dictionary, and math to perform log base e operation
from nltk import tokenize
from operator import itemgetter
import math


#2. Remove stopwords: we use the nltk library to remove stopwords
#stopwords are the frequently occuring words that won't carry significance to our analysis
import nltk
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
stop_words = set(stopwords.words('english'))

#3. Reading CSV file line-by-line and assigning this as the value of string variable doc
def readFile(fileName): #reads file and gets rid of punctuation
    a = ""
    with open(fileName, encoding='UTF-8') as f:
        for line in csv.reader(f):
            s = str(line)
            #no_punc = s.translate(str.maketrans('','', string.punctuation))
            #print(s)
            a = a + s
    
    return a

#doc = readFile('p2.csv')
doc = "I am a graduate. I want to learn Python. I like learning Python. Python is easy. Python is interesting. Learning increases thinking. Everyone should invest time in learning"

#4. finds total words in the document
total_words = doc.split() #splits words into arrays, but groups punctuations together and puts elements that have punctuations in double quotes
print(total_words)
total_word_length = len(total_words)
print(total_word_length)
#required while calculating term frequency

#5. finds total sentences in the document
total_sentences = tokenize.sent_tokenize(doc)
total_sent_len = len(total_sentences)
print(total_sent_len)
#required while calculating inverse document

#6. calculating total frequency for each word
tf_score = {}
for each_word in total_words:
    each_word = each_word.replace('.', '')
    if each_word not in stop_words:
        if each_word in tf_score:
            tf_score[each_word] += 1
        else:
            tf_score[each_word] = 1

#Dividing by total_word_length for each dictionary element
tf_score.update((x, y/int(total_word_length)) for x, y in tf_score.items())
print(tf_score)

#7. Function to check if the word is present in a sentence list
def check_sent(word, sentences): 
    final = [all([w in x for w in word]) for x in sentences] 
    sent_len = [sentences[i] for i in range(0, len(final)) if final[i]]
    return int(len(sent_len))

#8. Calculate IDF for each word
idf_score = {}
for each_word in total_words:
    each_word = each_word.replace('.','')
    if each_word not in stop_words:
        if each_word in idf_score:
            idf_score[each_word] = check_sent(each_word, total_sentences)
        else:
            idf_score[each_word] = 1

#Performing a log and divide
idf_score.update((x, math.log(int(total_sent_len)/y)) for x, y in idf_score.items())

print(idf_score)

#9. Calculate TF*IDF
tf_idf_score = {key: tf_score[key] * idf_score.get(key, 0) for key in tf_score.keys()}
print(tf_idf_score)

#10. Create a function to get N important words in the document
def get_top_n(dict_elem, n):
    result = dict(sorted(dict_elem.items(), key = itemgetter(1), reverse = True)[:n]) 
    return result

#11. Get the top 5 words of significance
print(get_top_n(tf_idf_score, 5))

'''Did what I wanted it to in terms of functionality but only good for a large corpus (i.e. large text file)'''