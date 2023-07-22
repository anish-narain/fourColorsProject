def cosine_bert_calculator(queryString, folder_name):
    from sentence_transformers import SentenceTransformer
    from sklearn.metrics.pairwise import cosine_similarity
    from pathlib import Path
    from collections import Counter
    import csv

    sbert_model = SentenceTransformer('bert-base-nli-mean-tokens')
    top_value = 0
    suggested_link =''
    matching_dictionary = {}

    #analysis_files is (for simplicity) an array of the textfiles in folder_name directory 
    #(which is second parameter of this function)
    analysis_files =  Path(folder_name).glob('*.txt')
    #for each text file within the array of textfiles
    for file in analysis_files:
        text = open(file, "r").read()
        #creates another array which stores user input and contents of that text file
        sentences = [queryString, text]
        #this is the code to generate bert vector
        #bert vector can be thought of as a tree. If you put in a sentence like "This movie had a sinister plot", 
        #BERT would look at this sentence from left to right and right to left (bi-directional) to create two trees for the two sentences
        sentence_embeddings = sbert_model.encode(sentences)

        #cosine similarity looks at how similar the two trees are
        #the cosine_similarity function returns an nxn matrix which is stores in cos_sim
        cos_sim = cosine_similarity(sentence_embeddings)
        
        #the weighting of cosine similarity is in position [0][1] of matrix
        sim_value = cos_sim[0][1]
        #this removes the '.txt' part of the file name (we could do this since the lengths of the hashed names are fixed)
        name_of_file = file.name[:32]
        #we create a dictionary (key value is name_of_file and corresponding data is sim_value)
        matching_dictionary[name_of_file] = [sim_value]

    #pulls out 3 file names having the highest sim value (meaning the 3 files that have the strongest match with the query)
    k = Counter(matching_dictionary)
    high = k.most_common(3)
    
    #the previous code returns the FILENAME but we want the URL for that filename
    #we use the cross reference text file to get the corresponding urls for the three top files
    for i in high:
        with open('cross-reference.txt') as inf:
            reader = csv.reader(inf)
            for row in reader:
                if row[1] == i[0]:
                    suggested_link = row[0]
                    print(suggested_link," :",i[1]," ")
