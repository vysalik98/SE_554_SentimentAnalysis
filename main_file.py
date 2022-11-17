import streamlit as st
import pickle
from program.class_def import AntonymReplacer

st.title('Sentiment Analysis Tool')

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
    st.write('Please enter text')
