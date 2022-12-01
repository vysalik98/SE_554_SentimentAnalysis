#########################################################################################
# Title : sentiment_analysis
# 
# Team/Authors        
# ***************
# 1. Vysali
# 2. Prachi
# 3. Saurav
# 
#   
# Purpose     : Implementing code for Sentiment Analysis    
# Environment : Venv (Dependencies in requirements.txt)
# Usage       : python3 sentiment_analysis_functions.py
#########################################################################################

import nltk
from nltk.corpus import wordnet
from nltk.tokenize import word_tokenize

import pandas as pd
from spacy.lang.en.stop_words import STOP_WORDS

import string
import spacy

nltk.download('punkt')
nltk.download('wordnet')
nltk.download('omw-1.4')

class SentimentAnalysis():

  def __init__(self) -> None:
    self.punct = string.punctuation
    self.nlp = spacy.load('en_core_web_sm')
    self.stopwords = list(STOP_WORDS)
    self.filename = '/Users/vysalikallepalli/Downloads/Github/SE_554_SentimentAnalysis/data/IMDB_Dataset.csv'


  # This method provide antonym nltk library
  def get_antonym(self, word):
    antonyms = []
    for syn in wordnet.synsets(word):
      for lemma in syn.lemmas():
        if lemma.antonyms():
          antonyms.append(lemma.antonyms()[0].name())
    if len(antonyms) >= 1:
      return antonyms[0]
    else:
      return None
    
  # This method replaces the not word from the sentences with antonym
  def replace_neg(self,string):
    i=0
    sent = word_tokenize(string)
    
    len_sent = len(sent)
    words = []
    sentence = ''
    while i < len_sent:
      word = sent[i]
      if word == 'not' and i+1 < len_sent:
        ant = self.get_antonym(sent[i+1]) 
        if ant:
          words.append(ant)
          sentence += ant + " "
          i+=2
          continue
      words.append(word)
      sentence += word + " "
      i+=1
    return sentence

  def text_data_cleaning(self, sentence):
    # This method cleans up the data with respect to stop words and punctuations
    doc = self.nlp(self.replace_neg(sentence))
    tokens = []
    for token in doc:
      if token.lemma_ != "-PRON-":
        temp = token.lemma_.lower().strip()
      else:
        temp = token.lower_
      tokens.append(temp)
    cleaned_tokens = []
    for token in tokens:
      if token not in self.stopwords and token not in self.punct:
        cleaned_tokens.append(token)
    return (cleaned_tokens)
  
  def readcsv(self):
     # This method reads the file
    data = pd.read_csv(self.filename, header=None)
    data.head()
    print(data.shape)
    x = data[0]
    y = data[1]
    return x, y


if __name__ == '__main__':
  # main()
  object = SentimentAnalysis()
  execute = object.replace_neg("I did not like it")
  print(str(execute))
