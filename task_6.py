# Task 6

# Write the Task 5 titles to the text file.

# Extras:
# Ask the user to specify the name of the output file that will be saved.

# Import libraries
import requests
from bs4 import BeautifulSoup

# Collect first page of news list
page = requests.get('https://news.ycombinator.com/')
# Create a BeautifulSoup object
soup = BeautifulSoup(page.text, 'html.parser')
# Pull all text from the itemlist class
news_name = soup.find(class_='itemlist')
# Pull text from all instances of storylink class within itemlist class
news_name_items = news_name.find_all(class_='storylink')
print("-" * 40)
user_file = input(" Please enter the file name - ")  # Taking file name input from the user
file1 = open(user_file + ".txt", "w")
print("-" * 40)

# Create for loop to print out all news titles
for news in news_name_items:
    names = news.contents[0]
    print(names)
    file1.write(names + '\n')

print("-" * 40)
print("File ",user_file," successfully generated. ")
print("-" * 40)
file1.close()
