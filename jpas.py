import streamlit as st
import requests
import os
import time
from streamlit_extras.tags import tagger_component
from PIL import Image

# Store the initial value of widgets in session state
if "visibility" not in st.session_state:
    st.session_state.visibility = "visible"
    st.session_state.disabled = False

# Show main banner
image = Image.open('banner.jpg')
st.image(image)

# Configure layout
left_column, right_column = st.columns(2)

# Set API to call
url = os.environ['BACKEND_HOST']
# url = "192.168.2.11"  # for local testing
api = "http://" + url + ":8910/ml"

with st.container():
    tags = {"keywords": ['example 1', 'example 2']}
    with left_column:
        st.header('More than an AI keyword extraction.')
        st.caption('Empowering job seekers to increase their chances of landing their dream job. JPAS leverages NLP AI models to extract keywords from job postings.')

    with right_column:
        image1 = Image.open('picture.jpg')
        st.image(image1)

st.subheader("Enter job posting description")
text_input = st.text_area(
    "Paste text here 👇",
    label_visibility=st.session_state.visibility,
    disabled=st.session_state.disabled,
    height=300
)

if st.button('Get keywords'):
    with st.spinner('Processing...'):
        data = [{"position": "position", 'jobDescription': text_input}]
        response = requests.post(api, json=data)
        try:
            tags = response.json()
        except requests.exceptions.RequestsJSONDecodeError as e:
            print(f"Error decoding JSON: {e}")
        st.success('Done!')


st.caption('Keywords:')
colors = ['lightblue', 'orange', 'bluegreen',
          'blue', 'violet', 'red', 'green', 'yellow']
print(type(tags))
print(len(tags['keywords']))
colors_lista = []
for i in range(len(tags['keywords'])):
    colors_lista.append(colors[i % (len(colors))])
tagger_component(
    " ",
    tags['keywords'],
    color_name=colors_lista
)
