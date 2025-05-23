# Naptick RAG Memory Chatbot

## 🚀 Overview

This project is a fully functional AI-powered chatbot designed for the Naptick AI Challenge — Task 1: Multi-Collection RAG System with Memory Layer.

The chatbot uses **Retrieval-Augmented Generation (RAG)** over **five diverse data collections**, integrated with a **memory layer** to preserve conversational context across sessions.

---


## 🧠 Key Features

- **Multi-collection data indexing** (Wearables, Chat, Profile, Location, Research)
- **Custom embedding + chunking pipeline** using LangChain + OpenAI
- **Contextual memory support** for follow-up conversations
- **Modular RAG pipeline** with clean abstractions
- **CLI + Streamlit-based Web Demo**

---

## 🗂️ Data Collections (Simulated)

1. `wearable_data.json` – Sleep duration, REM, heart rate
2. `chat_history.json` – Previous user queries and timestamps
3. `user_profile.json` – Age, gender, preferences
4. `location_data.json` – Geo-tags and timestamps
5. `custom_collection.json` – Research summaries and articles

---

## 🛠️ Tech Stack

| Component     | Tool/Library            |
|---------------|-------------------------|
<<<<<<< HEAD
| LLM           | OpenAI (via API)|
=======
| LLM           |  OpenAI(via API)|
>>>>>>> b4c584abe129c470ebafb61da5ef32dde6ffc97c
| Embeddings    | `OpenAIEmbeddings`      |
| Vector Store  | `ChromaDB`              |
| Memory Layer  | `LangChain.Memory`      |
| UI Interface  | CLI + Streamlit         |
| Data Format   | JSON (simulated)        |

---

## 🧩 Directory Structure

```
naptick-rag-memory-chatbot/
├── data/                 # All 5 data sources in JSON
├── src/                  # Modular source code
├── requirements.txt
├── README.md
<<<<<<< HEAD

=======
         
>>>>>>> b4c584abe129c470ebafb61da5ef32dde6ffc97c
```

---

## ✅ Setup & Running

### 1. Install Dependencies

```bash
pip install -r requirements.txt
```

### 2. Set Your OpenAI API Key

```bash
export OPENAI_API_KEY=your_key_here
```

### 3. Run CLI Chatbot

```bash
python src/chatbot_cli.py
```

### 4. Run Streamlit Web UI

```bash
streamlit run src/chatbot_web.py
```

---

## 🧠 Example Queries

- "What was my average REM sleep last week?"
- "Show me any advice based on my profile preferences."
- "Did my travel to Toronto affect sleep?"

---

## 📄 Deliverables

This submission includes:

- Complete codebase (`/src`) with modular files
- Simulated JSON collections (`/data`)
- Working CLI + Web App (`chatbot_cli.py`, `chatbot_web.py`)
- PDF Write-up (pending)
- Clean, documented, extensible logic

---

## 💡 Future Work

- Proactive reminders using memory-based triggers
- Nightly sleep summaries from wearable + profile synthesis
- Graphical insights in UI for visual tracking


---

**Made with ❤️ for Naptick by [Sahej Preet Singh]**
