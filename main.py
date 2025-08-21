import streamlit as st



Usr_Str =st.text_input("Sentiment checker", value="", max_chars=None, type="default", help=None, autocomplete=None, on_change=None, args=None, kwargs=None,  placeholder="Please enter your sentance here", disabled=False, label_visibility="visible", icon=None, width="stretch")

st.session_state.Usr_Str = Usr_Str

uploaded_file = st.file_uploader("Upload a text file", type=["txt"])

if uploaded_file is not None:
    Usr_Str = uploaded_file.read().decode("utf-8")
    st.text_area("Text", Usr_Str, height=300)



video_file = st.file_uploader("Upload a video file", type=["mp4", "avi", "mov", "mkv"])

if video_file is not None:
    # Display video file details
    file_details = {
        "Filename": video_file.name,
        "FileType": video_file.type,
        "FileSize": f"{video_file.size / 1024 / 1024:.2f} MB"
    }
    st.write("File Details:", file_details)
    
    # Display the video
    st.video(video_file)



if st.button("Go to Results Page ➡️"):
    
    st.switch_page("pages/page_1.py")
    


