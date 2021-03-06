from textblob import TextBlob
import sys
import tweepy
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
import os
import nltk
import pycountry
import re
import string
from wordcloud import WordCloud, STOPWORDS
from PIL import Image
from nltk.sentiment.vader import SentimentIntensityAnalyzer
from langdetect import detect
from nltk.stem import SnowballStemmer
from nltk.sentiment.vader import SentimentIntensityAnalyzer

from sklearn.feature_extraction.text import CountVectorizer


#creating PieCart
 
 labels = ['positive'+str(positive)+'%'] , 'Neutral'+str(neutral+'%]','Negative'+str(negative)+'%] ']


 sizes = [positive,neutral,negative]
 

 colors = ['yellowgreen','blue','red']

 patches ,texts = plt.pie(sizes,colors=colors,startangle=90)

 plt.style.use('default')

 plt.legend(labels)

 plt.title("Sentiment Analysis  result for keyword= "+keyword+"')
 plt.axis ('equal')
 plt.show()