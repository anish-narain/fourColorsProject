#Import libraries
import requests
from bs4 import BeautifulSoup 
from urllib.request import Request, urlopen
import csv
from csv import reader
from bs4 import SoupStrainer

files = [] #list that will contain all file names

def fetchUrl(row): #takes in csv row (which is a list) and extracts url from it (first element in the list)
    url = str(row[1]) #assigns list element as string type
    return url

def fileName(url): #takes in url and generates a name for its corresponding csv file
    txtHash = str(hash(url))
    txtEnd = '.txt'
    #urlFile = 'contentFiles//' + urlHash + csvEnd
    urlFile = txtHash + txtEnd
    return urlFile


def webScrape(url, urlFile): #takes in url, name of csv file, writes in all the content of url in csv file
    req = Request(url, headers={'User-Agent': 'Mozilla/5.0'})
    page = urlopen(req).read()

    only_right_content = SoupStrainer(class_="section_single_post section_single_post--faq")

    soup = BeautifulSoup(page, 'html.parser', parse_only=only_right_content)
    cleaned_content = soup.get_text().strip()
    

    #write into textfile
    textfile = (open(urlFile, 'w'))
    a = textfile.write(cleaned_content)
    textfile.close()


def generateCSV():
    #open file in read mode
    with open('test1.csv', 'r') as read_obj:
    # pass the file object to reader() to get the reader object
        csv_reader = reader(read_obj)
        # Iterate over each row in the csv using reader object
        for row in csv_reader:
            #row variable is a list that represents a row in csv
            csv_url = fetchUrl(row)
            csv_fileName = fileName(csv_url)
            print("Processing this url:", csv_url, " and file name: ", csv_fileName)

            files.append(csv_fileName)
            webScrape(csv_url, csv_fileName)


#main code
generateCSV()

