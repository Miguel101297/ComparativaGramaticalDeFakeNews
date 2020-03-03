with open('resumen.txt','r') as miarchivo:
    texto=miarchivo.read()

from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize

import string

stop_words=set(stopwords.words('spanish'))
word_tokens = word_tokenize(texto)

word_tokens = list(filter(lambda token: token not in string.punctuation,word_tokens))

filtro = []

for palabra in word_tokens: 
    if palabra not in stop_words:
        filtro.append(palabra)
        
print(word_tokens)
print(type(filtro))

from collections import Counter
from collections import OrderedDict

c=Counter(filtro)
print(c.most_common(10))

y=OrderedDict(c.most_common())

with open('politica1.txt', 'w' ) as f:
    for k,v in y.items():
        f.write(f'{k} {v}\n')
        
