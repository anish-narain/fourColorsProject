import yake
import csv
from pathlib import Path 

csv_folder = Path('contentFiles').glob('*.csv')

def readFile(fileName): #reads file and gets rid of punctuation
    a = ""
    with open(fileName, encoding='UTF-8') as f:
        for line in csv.reader(f):
            s = str(line)
            #no_punc = s.translate(str.maketrans('','', string.punctuation))
            #print(s)
            a = a + s
    
    return a

for file in csv_folder:
    text = readFile(file)
    nameOfFile = file.name
    kw_extractor = yake.KeywordExtractor()
    keywords = kw_extractor.extract_keywords(text)

    language = "en"
    max_ngram_size = 3
    deduplication_thresold = 0.9
    deduplication_algo = 'seqm'
    windowSize = 1
    numOfKeywords = 20

    custom_kw_extractor = yake.KeywordExtractor(lan=language, n=max_ngram_size, dedupLim=deduplication_thresold, dedupFunc=deduplication_algo, windowsSize=windowSize, top=numOfKeywords, features=None)
    keywords = custom_kw_extractor.extract_keywords(text)


    out_file = 'analysisFiles//' + nameOfFile
    contFile = csv.writer(open(out_file, 'w'))
    
    for kw in keywords:
        contFile.writerow(kw)