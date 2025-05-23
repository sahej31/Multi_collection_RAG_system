import streamlit as st
from src.rag_pipeline import create_chatbot
from src.build_vectorstores import create_vectorstore

vectorstores = [
    create_vectorstore("task1_data_100_entries/wearable_data.json", "wearable", "vs_store"),
    create_vectorstore("task1_data_100_entries/chat_history.json", "chat", "vs_store"),
    create_vectorstore("task1_data_100_entries/user_profile.json", "profile", "vs_store"),
    create_vectorstore("task1_data_100_entries/location_data.json", "location", "vs_store"),
    create_vectorstore("task1_data_100_entries/custom_collection.json", "custom", "vs_store")
]

chatbot = create_chatbot(vectorstores)

st.title("Naptick Sleep Assistant ")
user_query = st.text_input("Ask your question:")

if user_query:
    answer = chatbot.run(user_query)
    st.write("Bot:", answer)
