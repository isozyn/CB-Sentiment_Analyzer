import streamlit as st

st.set_page_config(
    page_title="Analysis Results",
    page_icon="📊",
)

st.title("Analysis Results")

# create a clock for each type of result we want to produce
colCon, colPie, colRea, colButtons = st.columns(4,border=True, width="stretch")

with colCon:
    st.subheader("Sentiment Analysis Results \n Negative")
    st.image("images/negative.png")

    st.write("Confidence score: 25%")

with colPie:
    st.subheader("Sentiment Distribution")
    # Placeholder for pie chart
    st.write("Here you can display a pie chart of the sentiment distribution.")

with colRea:
    st.subheader("Related Texts")
    # Placeholder for related texts
    st.write("Here you can display texts related to the input text.")

with colButtons:
    st.button("Download in json")

    st.button("Download in csv")


    if st.button("⬅️ Back to Home"):
        st.switch_page("main.py")