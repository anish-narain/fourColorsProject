import yake
import csv
from pathlib import Path

content_folder = Path('contentFiles').glob('*.txt')
header_folder =  Path('headerFiles').glob('*.txt')

for file in content_folder:
    text = open(file, "r").read()
    nameOfFile = file.name

    language = "en"
    max_ngram_size = 3
    deduplication_threshold = 0.5
    deduplication_algo = 'seqm'
    windowSize = 1
    numOfKeywords = 5

    custom_kw_extractor = yake.KeywordExtractor(lan=language, n=max_ngram_size, dedupLim=deduplication_threshold, dedupFunc=deduplication_algo, windowsSize=windowSize, top=numOfKeywords, features=None)
    keywords = custom_kw_extractor.extract_keywords(text)

    outputFile = 'analysisFiles//' + nameOfFile
    textFile = csv.writer(open(outputFile, 'w'))

    for kw in keywords:
        textFile.writerow(kw)

for file in header_folder:
    text = open(file, "r").read()
    nameOfFile = file.name

    language = "en"
    max_ngram_size = 3
    deduplication_threshold = 0.5
    deduplication_algo = 'seqm'
    windowSize = 1
    numOfKeywords = 3

    custom_kw_extractor = yake.KeywordExtractor(lan=language, n=max_ngram_size, dedupLim=deduplication_threshold, dedupFunc=deduplication_algo, windowsSize=windowSize, top=numOfKeywords, features=None)
    keywords = custom_kw_extractor.extract_keywords(text)

    outputFile = 'analysisFiles//' + 'header' + nameOfFile
    textFile = csv.writer(open(outputFile, 'w'))

    for kw in keywords:
        textFile.writerow(kw)
