import streamlit as st
import requests
import time
from streamlit_extras.tags import tagger_component
from PIL import Image

# Store the initial value of widgets in session state
if "visibility" not in st.session_state:
    st.session_state.visibility = "visible"
    st.session_state.disabled = False

image = Image.open('banner.jpg')
st.image(image)

# LAYOUT
left_column, right_column = st.columns(2)

# API url
api = "http://172.22.224.1:8910/regex"

with left_column:
    st.header('More than an AI keyword extraction.')
    st.caption('Empowering job seekers to increase their chances of landing their dream job. JPAS leverages NLP AI models to extract keywords from job postings.')

with right_column:
    st.caption("Enter job posting description")
    text_input = st.text_area(
        "Paste text here 👇",
        label_visibility=st.session_state.visibility,
        disabled=st.session_state.disabled,
    )

    if st.button('Get keywords'):
        with st.spinner('Processing...'):
            data = {'jobDescription': text_input}
            response = requests.post(api, json=data)
            rp = response.json()
            time.sleep(3)
            st.success('Done!')
            st.caption('Keywords:')
            tagger_component(
                " ",
                rp['keywords']
            )