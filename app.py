# Core Pkgs
from sys import displayhook
from click import style
import streamlit as st 

# NLP Pkgs
import spacy_streamlit
import spacy
from spacy import displacy
from textblob import TextBlob 
# nlp = spacy.load('blank')

import os
from PIL import Image


def main():
    st.title("Dashboard")
#     our_image = Image.open(os.path.join('SpaCy_logo.svg.png'))
# st.image(our_image)

    menu = ["General","Cooking","LifeStyle"]
    choice = st.sidebar.selectbox("Industries Model",menu)

    global raw_text
    raw_text = st.text_area("Your Text"," ")

    if st.button("Analyze"):
        st.subheader("Named Entity Recognition")
        if choice == "General":
            nlp = spacy.load('general')
            docx = nlp(raw_text)
            label = nlp.get_pipe('ner').labels
            # spacy_streamlit.visualize_ner(docx,labels=label,attrs=['text','label_'])
            render_ent = displacy.render(docx, style='ent', jupyter=False)
            st.markdown(render_ent, unsafe_allow_html=True)

        elif choice == "Cooking":
            nlp = spacy.load('Cooking')
            docx = nlp(raw_text)
            label_ner = nlp.get_pipe('ner').labels
            # spacy_streamlit.visualize_ner(docx,labels=label_ner)
            render_ent = displacy.render(docx, style='ent', jupyter=False)
            st.markdown(render_ent, unsafe_allow_html=True)
        
        elif choice == "LifeStyle":
            nlp = spacy.load('LifeStyle')
            docx = nlp(raw_text)
            label = nlp.get_pipe('ner').labels
            # spacy_streamlit.visualize_ner(docx,labels=label,attrs=['text','label_'])
            render_ent = displacy.render(docx, style='ent', jupyter=False)
            st.markdown(render_ent, unsafe_allow_html=True)


        st.subheader("Sentiment Analysis")
        blob = TextBlob(raw_text)
        result_sentiment = blob.sentiment
        st.success(result_sentiment)


if __name__ == '__main__':
    main()