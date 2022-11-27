import streamlit as st
import pickle
from program.class_def import AntonymReplacer
import base64

class Display:
    def __init__(self):
        st.title('Sentiment Analysis Tool')

    def image_local(image_file):
        with open(image_file, "rb") as image_file:
            encoded_string = base64.b64encode(image_file.read())
            st.markdown(
            f"""
            <style>
            .stApp {{
                background-image: url(data:image/{"jpg"};base64,{encoded_string.decode()});
                background-size: cover
             }}
            </style>
             """,
            unsafe_allow_html=True
        )
    image_local('image1a.jpg')

    def sentiment_calculator(self):  

        filename = 'program/test.pkl'
        with open(filename, 'rb') as picklefile:
            newpred = pickle.load(picklefile) 
        title = st.text_input('Your Text/ Phrase')
        if st.button('Check Sentiment'):
            if (newpred.predict([title])[0] == "positive"):
                st.success(newpred.predict([title])[0])
            else:
                st.warning(newpred.predict([title])[0])
        else:
            st.write('Please enter a text')

if __name__ == '__main__':
    ct = Display()
    ct.sentiment_calculator()