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

import pandas as pd
from sklearn.svm import LinearSVC
from sklearn.metrics import accuracy_score, classification_report, confusion_matrix
from sklearn.model_selection import train_test_split
from sklearn.pipeline import Pipeline
from sklearn.feature_extraction.text import TfidfVectorizer
from spacy.lang.en.stop_words import STOP_WORDS
import string
import spacy
import ssl
from nltk.tokenize import word_tokenize
from nltk.corpus import wordnet
import nltk

try:
    _create_unverified_https_context = ssl._create_unverified_context
except AttributeError:
    pass
else:
    ssl._create_default_https_context = _create_unverified_https_context

nltk.download('wordnet')


class SentimentAnalysis():
    def __init__(self):
        nltk.download('omw-1.4')
        nltk.download('punkt')

        try:
            _create_unverified_https_context = ssl._create_unverified_context
        except AttributeError:
            pass
        else:
            ssl._create_default_https_context = _create_unverified_https_context

        nltk.download('wordnet')

        self.punct = string.punctuation
        self.nlp = spacy.load('en_core_web_sm')
        self.doc = self.nlp("the movie was good")
        self.stopwords = list(STOP_WORDS)
        self.filename = '../data/export_dataframe.csv'

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
    def replace_neg(self, string):
        i = 0
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
                    i += 2
                    continue
            words.append(word)
            sentence += word + " "
            i += 1
            return sentence

    def text_data_cleaning(self, sentence):
        # doc = self.nlp(self.replace_neg(sentence))
        # 
        doc = self.nlp(sentence)

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
        data = pd.read_csv(self.filename, header=None)
        data.head()
        print(data.shape)
        x = data[0]
        y = data[1]
        return x, y

    def creatingPipeline(self):
        tfidf = TfidfVectorizer(tokenizer=self.text_data_cleaning)
        classifier = LinearSVC()
        clf = Pipeline([('tfidf', tfidf), ('clf', classifier)])
        return clf

    def Training(self):
        x, y = self.readcsv()
        X_train, X_test, y_train, y_test = train_test_split(
            x, y, test_size=0.2, random_state=42)
        training_pipeline = self.creatingPipeline()
        training_pipeline.fit(X_train, y_train)
        y_pred = training_pipeline.predict(X_test)
        training_pipeline.predict(["I am not happy"])
        print(training_pipeline)
        print(classification_report(y_test, y_pred))
        return training_pipeline


if __name__ == '__main__':
    # main()
    test = SentimentAnalysis()
    test.readcsv()
    test.creatingPipeline()
    model = test.Training()
