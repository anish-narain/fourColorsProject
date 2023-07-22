#beautiful soup is a html parsing manipulation program
from bs4 import BeautifulSoup
from bs4 import SoupStrainer
import requests
from urllib.request import Request, urlopen
import hashlib

#main faq url
faqLink = 'https://www.technia.co.uk/support/faqs/'

#hits the main faq link
faqReq = Request(faqLink, headers={'User-Agent': 'Mozilla/5.0'})
#faq Content is a string that stores all of the html content in page
faqContent = urlopen(faqReq).read()
faqSoup = BeautifulSoup(faqContent, 'html.parser')

#goes to the correct section of the html content with wanted class id below
faq_page_section = faqSoup.find(class_='section_faqs__list')
#fetches all html content with <a> tag and puts into array
faq_page_list_items = faq_page_section.find_all('a')

#create cross-reference text file, this will be used to store the url (pulled from the a tag) and its hash
xrefFile = (open('cross-reference.txt', 'w'))

#for each element in the array that contains html content with wanted class id
for faq_link in faq_page_list_items:
        #fetches url from the element
        link = faq_link.get('href')
        #generates a hash from the url, this is used for name of text file
        hashedLink = hashlib.md5(link.encode()).hexdigest()
        #creates name for the text files
        contentFile = 'contentFiles//' + hashedLink + '.txt'
        headerFile  = 'headerFiles//' + hashedLink + '.txt'

        #pulls the content within the <a> tag (which is the heading that each url is linked to)
        headerContent = faq_link.contents[0].strip()


        helpReq = Request(link, headers={'User-Agent': 'Mozilla/5.0'})
        helpContent = urlopen(helpReq).read()

        c = xrefFile.write(link + ',' + hashedLink + '\n')

        only_right_content = SoupStrainer(class_="section_single_post section_single_post--faq")
        helpSoup = BeautifulSoup(helpContent, 'html.parser', parse_only=only_right_content)
        cleaned_content = (helpSoup.get_text().strip())

        textfile = (open(contentFile, 'w'))
        a = textfile.write(cleaned_content)
        textfile.close()

        textfiletwo = (open(headerFile, 'w'))
        b = textfiletwo.write(headerContent)
        textfiletwo.close()
