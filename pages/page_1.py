import streamlit as st
from ImgSelector import Select_image
import plotly.express as px
import numpy as np
from analysis import analyze_text, multi_class_classification
from explanation import extract_keywords, explain_classification
from comparison import compare_sentiment



st.set_page_config(
page_title="Sentiment Analyzer",
page_icon="🌟",
layout="wide",
initial_sidebar_state="expanded"
)


st.title("Analysis Results")

# create a clock for each type of result we want to produce
colCon, colPie, colRea, colButtons = st.columns(4,border=True, width="stretch")

#This is when lee gives me code i can use
#Senti_Image = ImgSel.ImgSelector(Sentiment)




Usr_Str_list = st.session_state.get("Usr_Str_list", ["No input provided."])
Usr_Str = st.session_state.get("Usr_Str", "No input provided.")
sentiment_result = analyze_text(Usr_Str)
classification = multi_class_classification(Usr_Str)

for idx, Usr_Str in enumerate(Usr_Str_list, 1):
    st.header(f"Sentence {idx}")
    sentiment_result = analyze_text(Usr_Str)
    classification = multi_class_classification(Usr_Str)
    
    Senti_Image = Select_image(sentiment_result['sentiment'])
    
    colCon, colPie, colRea, colButtons = st.columns(4,border=True, width="stretch")


    with colCon:
        st.subheader("Sentiment Analysis Results \n"+sentiment_result['sentiment'])
        st.image(Senti_Image)

        st.write("Confidence score: " + str(int(sentiment_result['confidence']*100)) + "%")


    with colPie:
        labels = ["Positive", "Neutral", "Negative"]
        values = classification['confidence_scores']

        st.subheader("Sentiment Distribution")
        fig = px.pie(names=labels, values=values, title="Sentiment Distribution", hole=0.3)
        st.plotly_chart(fig)

    with colRea:
        st.subheader("Explanation")
        # Placeholder for related texts
        st.write(Usr_Str)

        explanation = explain_classification(Usr_Str)
        st.write(f" {explanation['explanation']}")

    st.markdown("---")  # Separator between sentences           

with colButtons:
    st.button("Download in json")

    st.button("Download in csv")


    if st.button("⬅️ Back to Home"):
        st.switch_page("main.py")