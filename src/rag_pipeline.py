from langchain.chat_models import ChatOpenAI
from langchain.chains import ConversationalRetrievalChain
from langchain.vectorstores import Chroma
from langchain.memory import ConversationBufferMemory

def create_chatbot(vectorstores):
    from langchain.retrievers import MergerRetriever
    retrievers = [vs.as_retriever() for vs in vectorstores]
    merged = MergerRetriever(retrievers=retrievers)
    memory = ConversationBufferMemory(memory_key="chat_history", return_messages=True)
    qa = ConversationalRetrievalChain.from_llm(
        llm=ChatOpenAI(temperature=0.6),
        retriever=merged,
        memory=memory,
        verbose=True
    )
    return qa