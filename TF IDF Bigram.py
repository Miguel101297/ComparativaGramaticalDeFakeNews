import nltk 
import re 
from sklearn.feature_extraction.text import CountVectorizer, TfidfVectorizer 
from nltk.corpus import stopwords 
from nltk.tokenize import word_tokenize 
import pandas as pd 
  

txt1 = [] 
with open('politica1.1.txt') as file: 
    txt1 = file.readlines() 
# Stopword removal  
stop_words = set(stopwords.words('spanish')) 
your_list = ['', '', '', ''] 
for i, line in enumerate(txt1): 
    txt1[i] = ' '.join([x for 
        x in nltk.word_tokenize(line) if 
        ( x not in stop_words ) and ( x not in your_list )]) 
      
# Getting bigrams  
vectorizer = CountVectorizer(ngram_range =(2, 2)) 
X1 = vectorizer.fit_transform(txt1)  
features = (vectorizer.get_feature_names()) 
print("\n\nX1 : \n", X1.toarray()) 
  
# Applying TFIDF 
# You can still get n-grams here 
vectorizer = TfidfVectorizer(ngram_range = (2, 2)) 
X2 = vectorizer.fit_transform(txt1) 
scores = (X2.toarray()) 
print("\n\nScores : \n", scores) 
  
# Getting top ranking features 
sums = X2.sum(axis = 0) 
data1 = [] 
for col, term in enumerate(features): 
    data1.append( (term, sums[0, col] )) 
ranking = pd.DataFrame(data1, columns = ['Palabra', 'puntuaje']) 
words = (ranking.sort_values('puntuaje', ascending = False)) 
print ("\n\nWords : \n", words.head(4)) 
