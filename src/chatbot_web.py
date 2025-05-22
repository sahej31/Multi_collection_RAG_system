import streamlit as st
from src.rag_pipeline import create_chatbot
from src.build_vectorstores import create_vectorstore

vectorstores = [
    create_vectorstore("data/wearable_data.json", "wearable", "vs_store"),
    create_vectorstore("data/chat_history.json", "chat", "vs_store"),
    create_vectorstore("data/user_profile.json", "profile", "vs_store"),
    create_vectorstore("data/location_data.json", "location", "vs_store"),
    create_vectorstore("data/custom_collection.json", "custom", "vs_store")
]

chatbot = create_chatbot(vectorstores)

st.title("Naptick Sleep Assistant 🤖")
user_query = st.text_input("Ask your question:")

if user_query:
    answer = chatbot.run(user_query)
    st.write("🧠 Bot:", answer)