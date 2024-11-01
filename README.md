# Smart Tagging For FAQs

[This project was created in a pre-LLM world]
 
This project was a prototype with the aims to automate the process of finding relevant FAQs based on user queries. It scrapes the main FAQ page of a website, extracts individual FAQs, and analyzes the content to generate keywords. It then uses BERT embeddings and cosine similarity to compare user queries with the FAQ content and provide the top 3 most relevant FAQ questions as output.

Google’s Cloud Natural Language API was considered but the project was for technical documents which do not always follow the standard conventions of speaking language. Instead, a statistical, keyword extraction method was chosen called YAKE (Yet Another Keyword Extractor).

<img width="300" alt="image" src="https://github.com/anish-narain/fourColorsProject/assets/69715492/e61e4863-6e35-463e-8015-185ff09f9365">

The provided Python code consists of four files that work together to scrape information from a website's FAQ page, extract keywords from the content, and then calculate the cosine similarity between user queries and the FAQ content using BERT embeddings. 

| File | Description |
| --- | --- |
| scraper.py | This file is responsible for scraping the main FAQ page of a website and extracting the links to individual FAQ answers. It uses BeautifulSoup library for parsing HTML content and requests library for making HTTP requests. |
| keywords-extractor.py | This file extracts keywords from the content of individual FAQ answers. It uses the YAKE (Yet Another Keyword Extractor) library for keyword extraction. The extracted keywords are then saved in CSV files for each FAQ question and answer. |
| cosinebert.py | This file contains a function cosine_bert_calculator that calculates the cosine similarity between a user query and the FAQ content using BERT embeddings. It reads the FAQ content from the specified folder and generates BERT embeddings for both the user query and each FAQ question. Then, it calculates the cosine similarity between the embeddings to find the most similar FAQ questions to the user query.|
| chat.py | This file interacts with the user to get their query as input. It then calls the cosine_bert_calculator function from cosinebert.py three times for different folders (FAQ questions, FAQ question keywords, and FAQ answer keywords) to find the top 3 most similar FAQ questions for each case.|
