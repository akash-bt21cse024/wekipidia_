import streamlit as st
import requests
pip install bs4
from bs4 import BeautifulSoup
st.title("SEARCH ON WEKIPEDIA")
var=st.text_input("write your model name ")
title = var.replace(' ','+')
link = 'https://www.google.com/search?q=' + title + '+wikipedia'

res = requests.get(link)
soup = BeautifulSoup(res.text,'html.parser')


for sp in soup.find_all('div'):
    try:
        link = sp.find('a').get('href')
        if ('en.wikipedia.org' in link):
            break
    except:
        pass
    
link = link[7:].split('&')[0]

res = requests.get(link)
soup = BeautifulSoup(res.text,'html.parser')

corpus = ''
for p in soup.find_all('p'):
    corpus += p.text
    corpus += '\n'
    
corpus = corpus.strip()

for i in range(500):
    corpus = corpus.replace('['+str(i)+']','')




button=st.button("search")

if button :
    st.write(corpus)
