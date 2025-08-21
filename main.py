import streamlit as st
import pandas as pd
import json


st.set_page_config(
page_title="Main Page",
page_icon="🏠",
layout="wide",
initial_sidebar_state="expanded"
)
Usr_Str =st.text_input("Sentiment checker", value="", max_chars=None, type="default", help=None, autocomplete=None, on_change=None, args=None, kwargs=None,  placeholder="Please enter your sentance here", disabled=False, label_visibility="visible", icon=None, width="stretch")


uploaded_file = st.file_uploader(
    "Upload a file",
    type=["txt", "csv", "pdf", "json", "docx", "xlsx"]
)
Usr_Str_list = []

if uploaded_file is not None:
    file_type = uploaded_file.name.split('.')[-1].lower()
    if file_type == "txt":
        Usr_Str = uploaded_file.read().decode("utf-8")
        Usr_Str_list = [line.strip() for line in Usr_Str.split('\n') if line.strip()]
    elif file_type == "csv":
        df = pd.read_csv(uploaded_file)
        # Assume first column contains sentences
        Usr_Str_list = df.iloc[:, 0].dropna().astype(str).tolist()
    elif file_type == "xlsx":
        df = pd.read_excel(uploaded_file)
        Usr_Str_list = df.iloc[:, 0].dropna().astype(str).tolist()
    elif file_type == "json":
        data = json.load(uploaded_file)
        # Assume it's a list of sentences or dict with a key 'sentences'
        if isinstance(data, list):
            Usr_Str_list = [str(x) for x in data if str(x).strip()]
        elif isinstance(data, dict) and 'sentences' in data:
            Usr_Str_list = [str(x) for x in data['sentences'] if str(x).strip()]
else:
    Usr_Str_list = [line.strip() for line in Usr_Str.split('\n') if line.strip()]

st.session_state.Usr_Str = Usr_Str
st.session_state.Usr_Str_list = Usr_Str_list





if st.button("Go to Results Page ➡️"):
    
    st.switch_page("pages/page_1.py")
    


