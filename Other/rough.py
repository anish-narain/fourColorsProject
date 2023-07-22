#Import libraries
import requests
from bs4 import BeautifulSoup
import csv


#defines csv file with all urls
urlFile = csv.writer(open('url.csv', 'r'))

#create csv file to put the content into
contFile = csv.writer(open('page-content.csv', 'w'))


#collect url of web page using method requests.get() and store it in variable
page = requests.get('https://www.herschel.slough.sch.uk/Headteachers-Welcome')

#create a BeautifulSoup Object
soup = BeautifulSoup(page.text, 'html.parser')

#pull all text from the <div> tag where class (which is just its label) is 'content-area' into content_in_page variable
content_in_page = soup.find(class_ = 'content-area')
#pulls all the text within the <p> tag into content_in_ptag
content_in_ptag = content_in_page.find_all('p') #it doesn't, therefore pull text from <h2>, <style> etc just <p>

"""
#right now all the pulled <p> tags are squashed together in an array
#the for loop takes elements from the array and then prints them out one by one 
for content1 in content_in_ptag: 
    print(content1.prettify()) #the prettify() method turns the "parse tree" (parsed content) into nicely formatted Unicode string
"""

#for loop takes elements from the array and print them out one by one
#the .contents method returns the p tag's children as a python list data type (therefore removing the actual tag and just giving the words inside)
for content2 in content_in_ptag:
    paragraph = content2.contents[0]
    print(paragraph)
    print("") #add space between paragraphs

    contFile.writerow([paragraph]) #writes each paragraph into csv file


