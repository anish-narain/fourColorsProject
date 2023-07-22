from cosinebert import cosine_bert_calculator
queryString = input('What is your query? ')

print('\nNow calculating 3 top BERT+Cosine similarity between the query and the FAQ Question')
cosine_bert_calculator(queryString, 'faqQuestionContent')
#passes in (user input, path to folder)

print('\n\nNow calculating 3 top BERT+Cosine similarity between the query and the FAQ Question Keywords, extracted in step 3.')
cosine_bert_calculator(queryString, 'faqQuestionKeywords')

print('\n\nNow calculating 3 top BERT+Cosine similarity between the query and the FAQ Answer Keywords, extracted in step 3.')
cosine_bert_calculator(queryString, 'faqAnswerKeywords')
