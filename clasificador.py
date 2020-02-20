import csv
from textblob.classifiers import NaiveBayesClassifier
with open('categoria.json','r') as fp:
  cl=NaiveBayesClassifier(fp,format="json")
  print(cl.classify("Propone AMLO a Belinda para la Secretaría de Cultura ¡YA LE TIRÓ SU HUESO!"))
