# Task 5

# Use the BeautifulSoup and requests Python packages to print out a list of all the news titles on the https://news.ycombinator.com/.

# Import libraries
import requests
from bs4 import BeautifulSoup

# Collect first page of news list
page = requests.get('https://news.ycombinator.com/')

# Create a BeautifulSoup object
soup = BeautifulSoup(page.text, 'html.parser')

# Pull all text from the itemlist class
news_name_list = soup.find(class_='itemlist')

# Pull text from all instances of storylink class within itemlist class
news_name_list_items = news_name_list.find_all(class_='storylink') 

file1 = open("MyFile.txt","w")
# Create for loop to print out all news titles
for news in news_name_list_items:
    names = news.contents[0]
    print(names)
    file1.write(names+'\n')
file1.close()
