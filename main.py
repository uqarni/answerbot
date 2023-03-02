import nltk
nltk.download('punkt')

from langchain.document_loaders import UnstructuredFileLoader

loader = UnstructuredFileLoader("test.txt")

docs = loader.load()

test = docs[0].page_content[:400]
print(test)

