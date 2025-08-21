import streamlit as st
from ImgSelector import Select_image
import plotly.express as px
import numpy as np
from analysis import analyze_text, multi_class_classification
from explanation import extract_keywords, explain_classification
import json
import pandas as pd



st.set_page_config(
page_title="Sentiment Analyzer",
page_icon="🌟",
layout="wide",
initial_sidebar_state="expanded"
)


st.title("Analysis Results")

#This is when lee gives me code i can use
#Senti_Image = ImgSel.ImgSelector(Sentiment)




Usr_Str_list = st.session_state.get("Usr_Str_list", ["No input provided."])
Usr_Str = st.session_state.get("Usr_Str", "No input provided.")
sentiment_result = analyze_text(Usr_Str)
classification = multi_class_classification(Usr_Str)
results = []


for idx, Usr_Str in enumerate(Usr_Str_list, 1):
    sentiment_result = analyze_text(Usr_Str)
    classification = multi_class_classification(Usr_Str)
    explanation = explain_classification(Usr_Str)

    # Convert any numpy arrays to lists/floats
    confidence_scores = classification['confidence_scores']
    # If confidence_scores is a dict, convert its values to float
    if isinstance(confidence_scores, dict):
        confidence_scores = {k: float(v) if not isinstance(v, list) else [float(i) for i in v] for k, v in confidence_scores.items()}
    # If confidence_scores is a numpy array, convert to list of floats
    elif isinstance(confidence_scores, np.ndarray):
        confidence_scores = [float(x) for x in confidence_scores]

    results.append({
        "sentence": Usr_Str,
        "sentiment": str(sentiment_result['sentiment']),
        "confidence": float(sentiment_result['confidence']),
        "confidence_scores": confidence_scores,
        "explanation": str(explanation['explanation'])
    })

json_data = json.dumps(results, indent=2)
csv_data = pd.DataFrame(results).to_csv(index=False)
st.download_button(
    label="Download in json",
    data=json_data,
    file_name="sentiment_results.json",
    mime="application/json"
)

st.download_button(
    label="Download in csv",
    data=csv_data,
    file_name="sentiment_results.csv",
    mime="text/csv"
)

if st.button("⬅️ Back to Home"):
    st.switch_page("main.py")

for idx, Usr_Str in enumerate(Usr_Str_list, 1):
    st.header(f"Sentence {idx}")
    sentiment_result = analyze_text(Usr_Str)
    classification = multi_class_classification(Usr_Str)
    
    Senti_Image = Select_image(sentiment_result['sentiment'])
    
    colCon, colPie, colRea = st.columns(3,border=True, width="stretch")


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
