from langchain.document_loaders import TextLoader
from langchain.indexes import VectorstoreIndexCreator
import streamlit as st
import os
import openai

OPENAI_API_KEY = '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'
openai.api_key = OPENAI_API_KEY

# st.title("Document Bot")
# uploaded_file = st.file_uploader("Choose a file")

# if uploaded_file is not None:
#     with open("text.txt","wb") as f:
#         f.write(uploaded_file.getbuffer())
#     st.success("File uploaded")

# user_question = st.text_input(
#     "Enter Your Question : ",
#     placeholder = "Cyanobacteria can perform photosynthetsis , are they considered as plants?",
# )

# if st.button("Tell me about it", type = "primary"):
loader = TextLoader('text.txt')
index = VectorstoreIndexCreator().from_loaders([loader])
query = "What does FAIR stand for?"
answer = index.query_with_sources(query)
print(answer)
#     st.success(answer['answer'])


# os.system('streamlit run main.py --server.enableCORS false --server.enableXsrfProtection false')



