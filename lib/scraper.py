##from turtle import ht
from bs4 import BeautifulSoup
import requests

headers = {'user-agent': 'my-app/0.0.1'}
html = requests.get("https://flatironschool.com/", headers=headers)

doc = BeautifulSoup(html.text, 'html.parser')

#print(doc.select('.heading-50-black')[0].contents)

'''
titles=(doc.select('.heading-50-black.color-black'))
for title in titles:
    print(title.contents[0].strip())
    '''

#name = doc.select('.heading-50-black')[0].name
#print(name)

attrs = doc.select('.heading-50-black')[0].attrs
print(attrs)