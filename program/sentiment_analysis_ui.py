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
# Usage       : streamlit run sentiment_analysis_ui.py
#########################################################################################

import streamlit as st
import pickle
from sentiment_analysis_functions import SentimentAnalysis
import base64

class Display:
    def __init__(self):
        st.title('Sentiment Analysis Tool')

    #Calculation of the sentiments
    def sentiment_calculator(self):  

        filename = ''
        with open("./model.pkl", 'rb') as picklefile:
            newpred = pickle.load(picklefile) 
        title = st.text_input('Your Text/ Phrase')
        if st.button('Check Sentiment'):
            if (newpred.predict([title])[0] == "1"):
                st.success("Positive")
            else:
                st.warning("Negative")
        else:
            st.write('Please enter a text')

if __name__ == '__main__':
    ct = Display()
    ct.sentiment_calculator()
