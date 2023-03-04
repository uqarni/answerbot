from langchain.document_loaders import TextLoader
from langchain.indexes import VectorstoreIndexCreator
import openai
import os 
import streamlit as st

apikey = os.environ['OPENAI_API_KEY']
openai.api_key = apikey


st.title("Document Bot")

uploaded_file = st.file_uploader("Choose a file")
if uploaded_file is not None:
    # Open a file to write the contents of the uploaded file
    with open("text.txt", "wb") as f:
        f.write(uploaded_file.getbuffer())
    st.success("File saved as text.txt!")

user_question = st.text_input(
    "Enter Your Question : ",
    placeholder = "Cyanobacteria can perform photosynthetsis , are they considered as plants?",
)

if os.path.exists("text.txt"):
    loader = TextLoader('text.txt')
    index = VectorstoreIndexCreator().from_loaders([loader])

if st.button("Tell me about it", type = "primary"):
    query = user_question
    answer = index.query_with_sources(query)
    st.success(answer['answer'])

