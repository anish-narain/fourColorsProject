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
    urlHash = str(hash(url))
    csvEnd = '.csv'
    #urlFile = 'contentFiles//' + urlHash + csvEnd
    urlFile = "Test" + csvEnd
    return urlFile


def webScrape(url, urlFile): #takes in url, name of csv file, writes in all the content of url in csv file
    #create csv file to put the content into
    contFile = csv.writer(open(urlFile, 'w'))

    req = Request(url, headers={'User-Agent': 'Mozilla/5.0'})
    page = urlopen(req).read()
    soup = page_soup(page, 'html.parser')

    #pull all text from the <div> tag where class (which is just its label) is 'content-area' into content_in_page variable
    content_in_page = soup.find(class_ = 'section_single_post__body')
    #pulls all the text within the <p> tag into content_in_ptag
    content_in_ptag = content_in_page.find_all('p') #it doesn't, therefore pull text from <h2>, <style> etc just <p>

    #for loop takes elements from the array and print them out one by one
    #the .contents method returns the p tag's children as a python list data type (therefore removing the actual tag and just giving the words inside)
    for content2 in content_in_ptag:
        #paragraph = content2.contents[0]
        contFile.writerow(content2) #writes each paragraph into csv file
    

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

