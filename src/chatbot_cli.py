from src.build_vectorstores import create_vectorstore
from src.rag_pipeline import create_chatbot

vectorstores = [
    create_vectorstore("data/wearable_data.json", "wearable", "vs_store"),
    create_vectorstore("data/chat_history.json", "chat", "vs_store"),
    create_vectorstore("data/user_profile.json", "profile", "vs_store"),
    create_vectorstore("data/location_data.json", "location", "vs_store"),
    create_vectorstore("data/custom_collection.json", "custom", "vs_store")
]

chatbot = create_chatbot(vectorstores)

while True:
    query = input("You: ")
    if query.lower() in ["exit", "quit"]:
        break
    print("Bot:", chatbot.run(query))