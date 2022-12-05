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

    def StaticUI(self):
        st.title('Sentiment Analysis Tool')
        st.subheader('Abstract')
        st.markdown("Sentiment analysis is the use of natural language processing and text analysis to systematically identify, extract, quantify, and study affective states and subjective information.")

        st.subheader('Use Cases')
        col1, col2, col3 = st.columns(3)

        with col1:
            st.subheader("Social Media")

        with col2:
            st.subheader("customer response")

        with col3:
            st.subheader("customer service")

        st.markdown("""<hr style="height:10px;border:none;color:#333;background-color:tomato;" /> """, unsafe_allow_html=True)
        st.subheader('Try Here')
        self.sentiment_calculator()

    #Calculation of the sentiments
    def sentiment_calculator(self):  

        with open("./model.pkl", 'rb') as picklefile:
            newpred = pickle.load(picklefile) 
        title = st.text_input('Your Text/ Phrase')
        if st.button('Check Sentiment'):
            print(type(newpred.predict([title])[0]))
            if (newpred.predict([title])[0] == "1"):
                st.success("Positive")
            
            elif(newpred.predict([title])[0] == "0"):
                st.warning("Negative")
        else:
            st.write('Please enter a text')

if __name__ == '__main__':
    ct = Display()
    ct.StaticUI()

    
