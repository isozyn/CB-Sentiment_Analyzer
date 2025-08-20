import streamlit as st



Usr_Str =st.text_input("Sentiment checker", value="", max_chars=None, type="default", help=None, autocomplete=None, on_change=None, args=None, kwargs=None,  placeholder="Please enter your sentance here", disabled=False, label_visibility="visible", icon=None, width="stretch")

st.session_state.Usr_Str = Usr_Str

uploaded_file = st.file_uploader("Upload a text file", type=["txt"])

if uploaded_file is not None:
    Usr_Str = uploaded_file.read().decode("utf-8")
    st.text_area("Text", Usr_Str, height=300)





if st.button("Go to Results Page ➡️"):
    
    st.switch_page("pages/page_1.py")
    

