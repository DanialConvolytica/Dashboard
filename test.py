from curses import raw
from typing import List, Sequence, Tuple, Optional
from unittest.mock import sentinel

import pandas as pd
import streamlit as st
import spacy
from spacy import displacy
from textblob import TextBlob 


st.title("Dashboard")

menu = ["General","Cooking","LifeStyle","Food","Education","Travel","Parenting"]
choice = st.sidebar.selectbox("Industries Model",menu)

# global raw_text
raw_text = st.text_area("Your Text"," ")

if st.button("Analyze"):

    def get_html(html: str):
        """Convert HTML so it can be rendered."""
        WRAPPER = """<div style="overflow-x: auto; border: 1px solid #e6e9ef; border-radius: 0.25rem; padding: 1rem; margin-bottom: 2.5rem">{}</div>"""
        html = html.replace("\n", " ")
        return WRAPPER.format(html)

    def visualize_ner(
        doc: spacy.tokens.Doc,
        *,
        labels: Sequence[str] = tuple(),
        title: Optional[str] = "Named Entities",
        sidebar_title: Optional[str] = "Named Entities",
        key=None,
    ) -> None:

        """Visualizer for named entities."""
        if title:
            st.header(title)
        if sidebar_title:
            st.sidebar.header(sidebar_title)
        label_select = st.sidebar.multiselect(
            "Entity labels", options=labels, default=list(labels), key=key
        )
        style = "<style> mark.entity { display: inline-block }</style>"
        render_ent = displacy.render(docx, style='ent', jupyter=False)
        st.markdown(render_ent, unsafe_allow_html=True)    

    def sentence_analysis(path,text):
        """Sentence Analysis """
        st.subheader("Sentence Analysis ")
        sentiment = (path,raw_text)
        intent = (path,raw_text)
        emotion = (path,raw_text)
        language = (path,raw_text)
        


    if choice=='General':
        nlp = spacy.load('general')
        docx = nlp(raw_text)
        visualize_ner(docx, labels=nlp.get_pipe("ner").labels, key=1)

    elif choice=='Cooking':
        nlp = spacy.load('Cooking')
        docx = nlp(raw_text)
        visualize_ner(docx, labels=nlp.get_pipe("ner").labels, key=1)

    elif choice=='LifeStyle':
        nlp = spacy.load('LifeStyle')
        docx = nlp(raw_text)
        visualize_ner(docx, labels=nlp.get_pipe("ner").labels, key=1)

    elif choice=='Food':
        nlp = spacy.load('food')
        docx = nlp(raw_text)
        visualize_ner(docx, labels=nlp.get_pipe("ner").labels, key=1)

    elif choice=='Education':
        nlp = spacy.load('education')
        docx = nlp(raw_text)
        visualize_ner(docx, labels=nlp.get_pipe("ner").labels, key=1)

    elif choice=='Travel':
        nlp = spacy.load('travel')
        docx = nlp(raw_text)
        visualize_ner(docx, labels=nlp.get_pipe("ner").labels, key=1)

    elif choice=='Parenting':
        nlp = spacy.load('parenting')
        docx = nlp(raw_text)
        visualize_ner(docx, labels=nlp.get_pipe("ner").labels, key=1)