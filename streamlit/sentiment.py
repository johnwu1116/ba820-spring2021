# imports
import streamlit as st
import pandas as pd
from afinn import Afinn
import spacy
from spacy import displacy

HTML_WRAPPER = """<div style="overflow-x: auto; border: 1px solid #e6e9ef; border-radius: 0.25rem; padding: 1rem; margin-bottom: 2.5rem">{}</div>"""


MODEL = "en_core_web_sm"

# spacy.cli.download(MODEL)

### ok, we have that model, lets build our own
nlp = spacy.load(MODEL)



QST_URL = "https://d3bnk79bkod1sv.cloudfront.net/Organization/bb6b7239-a535-4050-bc6c-a59f00eed84b/Images/05daccbc-5ab8-4572-a004-55c3d13ea965.png"
st.image(QST_URL, use_column_width=True)

st.title('Test your data!')


st.markdown("You could imagine that we could use a very simple tool, like below, to validate input from models and other external datasets")

# Check your customer's statement here:
# user_input = st.text_area("label goes here", default_value_goes_here)
user_input = st.text_area("What is the text you want to verify")

afinn = Afinn(language='en')


if st.button('Submit'):
    score = afinn.score(user_input)
    st.markdown("----")
    st.write('Sentiment Score (afinn):  %s' % score)
    
st.markdown("----")

st.markdown("## NER via spacy")

ner_input = st.text_area("What message do you want to evaluate for entities?")

if st.button('Extract Entities'):
    doc = nlp(ner_input)
    html = displacy.render(doc, style="ent")
    st.write(HTML_WRAPPER.format(html), unsafe_allow_html=True)