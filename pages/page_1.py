import streamlit as st
from ImgSelector import Select_image
import plotly.express as px

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

Senti_Image = Select_image("negative")
Usr_Str = st.session_state.get("Usr_Str", "No input provided.")


with colCon:
    st.subheader("Sentiment Analysis Results \n Negative")
    st.image(Senti_Image)

    st.write("Confidence score: 25%")

with colPie:
    labels = ["Positive", "Neutral", "Negative"]
    values = [45, 30, 25]

    st.subheader("Sentiment Distribution")
    fig = px.pie(names=labels, values=values, title="Sentiment Distribution", hole=0.3)
    st.plotly_chart(fig)

with colRea:
    st.subheader("Related Texts")
    # Placeholder for related texts
    st.write(Usr_Str)
             

with colButtons:
    st.button("Download in json")

    st.button("Download in csv")


    if st.button("⬅️ Back to Home"):
        st.switch_page("main.py")