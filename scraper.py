#Beautiful soup is a html parser that helps extract html-based content 
from bs4 import BeautifulSoup
#Soup strainer allows you extract content from a specific subsection of the html page (it gets rid of header and footer)
from bs4 import SoupStrainer
#used to deal with http call
import requests
from urllib.request import Request, urlopen
import hashlib

#url of main FAQ page which contains all the answer links
faqLink = 'https://www.technia.co.uk/support/faqs/'

#Request() makes a http request (i.e. to access the contents in faqLink from the server it is hosted on)
#had to add headers={...} to mimic Mozilla browser call because website was rejecting requests without user agent header
faqReq = Request(faqLink, headers={'User-Agent': 'Mozilla/5.0'})
#extracts the http response (i.e. html code of the main FAQ page) and puts it into this variable
faqContent = urlopen(faqReq).read()
#this entire process was to extract the content that will be fed into BeautifulSoup

#to not have to write BeautifulSoup(...) every time we assign it to a variable
#faqSoup is an instance of the BeautifulSoup library
faqSoup = BeautifulSoup(faqContent, 'html.parser')
#(.find()) is a method of BeautifulSoup library that finds a wanted section of the html code
#this is assigned to faq_page_section (the section is identified using id 'section..')
faq_page_section = faqSoup.find(class_='section_faqs__list')
#(.find_all()) is a method that extracts specific html tags. Here we have extracted the <a> tags
#in order to get all the answer links within the main FAQ page
faq_page_list_items = faq_page_section.find_all('a')

#opens a textfile which we will use later on
xrefFile = (open('cross-reference.txt', 'w'))

#faq_page_list_items contains all the <a> tag content within our wanted section
for faq_link in faq_page_list_items:
        #(get.()) is a method of BeautifulSoup which extracts the content in a tag
        #here we are extracting the url (from href) and assigning it to variable link
        link = faq_link.get('href')
        #to create unique filenames for each answer link we apply a hash function on the link
        hashedLink = hashlib.md5(link.encode()).hexdigest()
        #location of files:
        contentFile = 'faqAnswerContent//' + hashedLink + '.txt'
        headerFile  = 'faqQuestionContent//' + hashedLink + '.txt'
        #the 'faq...//' creates a path to the correct folder (directory), hashedLink is name of text file

        #faqLink is a row of faq_page_list_items
        #faqLink will look like  <a href = "url..."> TEXT </a>
        #headerContent stores that TEXT value
        headerContent = faq_link.contents[0].strip()
        #in our case, this is the heading of the answer webpage

        #Now make http request to the answer page (in the same way we did for the main FAQ page)
        helpReq = Request(link, headers={'User-Agent': 'Mozilla/5.0'})
        helpContent = urlopen(helpReq).read()
        #helpContent contains the entire answer webpage (from which I only need text from a single section)

        #created a cross referencing file to note down every link and its corresponding hash for reference later
        c = xrefFile.write(link + ',' + hashedLink + '\n')

        #the SoupStrainer() method ensures no footers and headers are included
        #it focuses on the section I want of the answer webpage
        only_right_content = SoupStrainer(class_="section_single_post section_single_post--faq")
        #helpSoup is an instance of BeautifulSoup library (to not have to write BeautifulSoup(...) every time)
        helpSoup = BeautifulSoup(helpContent, 'html.parser', parse_only=only_right_content)
        #strip() is used to get rid of blank spaces before and after the text
        #get_text() returns all the text in a document or beneath a tag, as a single Unicode string
        cleaned_content = (helpSoup.get_text().strip())

        #puts the content of the answer webpage in contentFile
        textfile = (open(contentFile, 'w'))
        a = textfile.write(cleaned_content)
        textfile.close()

        #puts header of answer webpage in headerFile
        textfiletwo = (open(headerFile, 'w'))
        b = textfiletwo.write(headerContent)
        textfiletwo.close()
        
#confirmation
print('Successfully extracted the information to faqQuestionContent and faqAnswerContent folders')
