# Domain-Specific-AI-Chatbot

# Data Science Companion — Domain-Specific AI Chatbot

A domain-restricted AI chatbot designed to answer **Data Science–related queries only**, built using **Google Gemini API**, **Streamlit**, and deployed on **AWS EC2**.

This project was developed as part of the **Data Science with Advanced Gen AI Internship at Innomatics Research Labs**, with the objective of building and deploying a controlled conversational AI system rather than a generic chatbot.

---

## Project Overview

**Data Science Companion** is an LLM-powered assistant that acts as a focused domain expert.
The chatbot responds exclusively to questions related to Data Science and politely refuses queries outside the domain.

The system demonstrates how prompt engineering, session memory, and cloud deployment can be combined to create a structured and production-style GenAI application.

---

## Features

* Domain-specific chatbot (Data Science only)
* Guardrail-based system prompt enforcement
* Multi-turn conversational memory
* Interactive Streamlit chat interface
* Secure API key management using environment variables
* Cloud deployment using AWS EC2
* Clean and modular application structure

---

## System Behavior

The chatbot follows strict rules:

* Answers **only Data Science-related questions**
* Rejects unrelated queries with a controlled response
* Maintains professional and consistent tone
* Preserves conversation history during the session

---

## Tech Stack

| Component              | Technology                |
| ---------------------- | ------------------------- |
| LLM                    | Google Gemini 2.5 Flash   |
| Backend                | Python                    |
| UI                     | Streamlit                 |
| Environment Management | python-dotenv             |
| Cloud Hosting          | AWS EC2 (Ubuntu)          |
| Deployment             | SSH + Virtual Environment |

---

## Project Architecture

```
User
  ↓
Streamlit Chat Interface
  ↓
Session State Memory
  ↓
Prompt Guardrails (Domain Restriction)
  ↓
Google Gemini API
  ↓
Generated Response
  ↓
Streamlit UI
```

---

## Project Structure

```
chatbot_deploy/
│
├── app.py              # Main Streamlit application
├── requirements.txt    # Project dependencies
├── .env                # Environment variables (not committed)
└── README.md
```

---

## 🌐 Live Deployment

The application is deployed on an AWS EC2 instance:

```
http://13.61.9.39:8501
```

> Note: The app uses HTTP (not HTTPS) for prototype deployment, so browsers may display a "Not Secure" warning.

---

## Learning Outcomes

This project focuses on practical GenAI system development:

* Prompt engineering with domain guardrails
* Managing conversational memory
* Secure API key handling
* Streamlit-based AI interfaces
* Linux server operations
* Cloud deployment using AWS EC2

---

Developed as part of the **Data Science with Advanced Gen AI Internship** at **Innomatics Research Labs**, emphasizing real-world AI application deployment and engineering practices.

