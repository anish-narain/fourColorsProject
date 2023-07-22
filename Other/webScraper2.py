#Import libraries
import requests
from bs4 import BeautifulSoup as page_soup
from urllib.request import Request, urlopen
import csv
from csv import reader

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
    soup = page_soup(page, 'html.parser')

    #remove bottom links
    last_links1 = soup.find(class_='sdrn_levels top sdrn_jquery')
    last_links1.decompose()


    content = soup.get_text()

    #get rid of empty lines within text file
    lines = content.split("\n")
    non_empty_lines = [line for line in lines if line.strip() != ""]
    cleaned_content = ""
    for line in non_empty_lines:
        cleaned_content += line + "\n"
    
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

