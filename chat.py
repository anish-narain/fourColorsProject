import yake
queryString = input('What is your query? ')

language = "en"
max_ngram_size = 3
deduplication_threshold = 0.1
deduplication_algo = 'seqm'
windowSize = 1
numOfKeywords = 3

custom_kw_extractor = yake.KeywordExtractor(lan=language, n=max_ngram_size, dedupLim=deduplication_threshold, dedupFunc=deduplication_algo, windowsSize=windowSize, top=numOfKeywords, features=None)
keywords = custom_kw_extractor.extract_keywords(queryString)
print('The keywords for this question are')
for kw in keywords:
    print(kw[0])
