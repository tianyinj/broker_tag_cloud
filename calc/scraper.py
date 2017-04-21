# -*- coding: UTF-8 -*-

import json
import requests
from lxml import html
from lxml.etree import tostring
import re
import logging
import sys
from bs4 import BeautifulSoup
import urllib2
from goose import Goose
from nltk import word_tokenize
import string


import sys
reload(sys)
sys.setdefaultencoding('utf-8')

CNBC_URL = "http://data.cnbc.com/quotes/"
CNN_URL = "http://money.cnn.com/quote/news/news.html?symb="

logger = logging.getLogger(__name__)


def run(index):
    r = urllib2.urlopen(CNN_URL+index).read()
    soup = BeautifulSoup(r,"lxml")
    headlines = []
    links = []
    articles = []
    print ("Start reading news for: "+ index)
    for div in soup.find_all('table', 'wsod_newsTable')[0]:
        for col in div:
            link = col.find('a')['href']
            headline = col.find('a').contents[0]
            g = Goose()
            articles.append(g.extract(url=link).cleaned_text)


    print ("Finished Reading!")
    tokens = []

    for article in articles:
        tokens += word_tokenize(article)
    tokens = filter(lambda word: word not in string.punctuation, tokens)
    result = []
    for word in set(tokens):
        if tokens.count(word)>20 and tokens.count(word)<100:
            result.append((word, tokens.count(word)))

    return result


if __name__ == "__main__":
   main(sys.argv)
