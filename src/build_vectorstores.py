from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain.vectorstores import Chroma
from langchain.embeddings import OpenAIEmbeddings
from src.load_data import load_json_as_documents

def create_vectorstore(json_file, source_label, persist_dir):
    docs = load_json_as_documents(json_file, source_label)
    splitter = RecursiveCharacterTextSplitter(chunk_size=500, chunk_overlap=50)
    chunks = splitter.split_documents(docs)

    return Chroma.from_documents(
        documents=chunks,
        embedding=OpenAIEmbeddings(),
        persist_directory=persist_dir,
        collection_name=source_label
    )