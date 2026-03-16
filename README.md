# Smart-Bot

A feature-rich Flask-based chatbot application with persistent MongoDB storage, session management, and local LLM integration via Ollama.

## Overview

Smart-Bot is an intelligent chat application that combines the power of local LLMs with robust data persistence. It provides users with a seamless chat experience while maintaining complete conversation history across sessions. Built with Flask and MongoDB, it offers real-time responses using the Mistral model running locally through Ollama.

## Features

- **Persistent Chat History**: All conversations stored in MongoDB for future reference
- **Session Management**: Unique session IDs for each user/visit
- **Dual History System**: 
  - Real-time conversation display
  - Dedicated history viewer for past messages
- **Local LLM Processing**: Privacy-focused with Mistral model via Ollama
- **Modern Chat Interface**: Clean, responsive design with loading animations
- **Session-Based Retrieval**: View complete chat history for your session
- **Error Handling**: Robust error management for LLM interactions

## Tech Stack

### Backend
- **Framework**: Flask with Flask-Session
- **Database**: MongoDB with Flask-PyMongo
- **LLM Framework**: LangChain with Ollama
- **AI Model**: Mistral (latest)
- **Session Storage**: Server-side filesystem

### Frontend
- **HTML5/CSS3**: Custom styling with animations
- **JavaScript**: Async/await API calls
- **UI Features**: Loading indicators, scroll management

## Prerequisites

- Python 3.8+
- MongoDB (local installation or Atlas)
- Ollama installed locally
- Mistral model pulled in Ollama

## Installation

1. **Clone the repository**
   ```bash
   git clone <repository-url>
   cd smart-bot
2. **Use Chatbot**
   ```bash
   step 1 : virtual environment --> python -m venv .venv
   step 2 : install requirements --> pip install flask langchain ollama flask flask-pymongo flask-session

