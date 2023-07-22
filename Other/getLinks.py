#Import libraries
import requests
from bs4 import BeautifulSoup as soup
import csv
from csv import reader
from urllib.request import Request, urlopen
import string

contFile = csv.writer(open('urlFile.csv', 'w'))
faqLink = 'https://www.technia.co.uk/support/faqs/'

req = Request(faqLink, headers={'User-Agent': 'Mozilla/5.0'})
page = urlopen(req).read()
page_soup = soup(page, 'html.parser')

questions_list = page_soup.find(class_ = 'section_faqs__list')
question_list_items = questions_list.find_all('a')

for question_item in question_list_items:
    question = question_item.contents[0]
    link = question_item.get('href')
    rowData = [question.strip(), link]
    #print(rowData)
    contFile.writerow(rowData)

