import os
from google import genai
from dotenv import load_dotenv
import streamlit as st

load_dotenv()

# configure Gemini API key from file
os.environ['GOOGLE_API_KEY'] = os.getenv('gemini')

# creating the client for Gemini
client = genai.Client()

# system prompt
system_prompt = '''You are a domain-specific assistant that ONLY answers questions related to Data Science. 
                   Your role is to provide accurate, clear, and helpful responses.
                   Strict rules:
                        1. If the user asks a question related to Data Science → provide a full, detailed, and helpful answer.
                        2. If the user asks a question outside Data Science → politely respond with:
                        "I can only answer queries related to Data Science. Please ask something in that domain."
                        3. Never attempt to answer or speculate on topics outside Data Science.
                        4. Always maintain a professional, clear, and supportive tone in your responses.'''

# Page Configuration
st.set_page_config(
    page_title = 'Your Data Science Companion',
    page_icon = '🤖',
    layout = 'centered'
)

# UI enhancement for better interface

st.markdown("""
    <style>
    .stChatMessage {
        padding: 12px;
        border-radius: 12px;
        margin-bottom: 8px;
    }
            
    .stChatMessage.user {
        background-color: #E8F0FE;
    }
        
    .stChatInputContainer {
        margin-top: 20px;
    }
            
    .block-container {
        padding-top: 2rem;   
    }
    </style>
""", unsafe_allow_html = True)

# Sidebar
with st.sidebar:
    st.header("📌 About This Bot")
    st.write("""
    - Powered by Gemini 2.5 Flash
    - Domain-Specific: Data Science Only
    - Multi-turn Conversation Memory
    """)

    if st.button('Clear Chat 🧹'):
        st.session_state.messages = [
            {'role':'system', 'content':system_prompt}
        ]
        st.rerun()

# main title
st.title("🤖 Your Data Science Companion")
st.markdown("Ask anything related to **Data Science...**")

# Initializing Session Memory
if 'messages' not in st.session_state:
    st.session_state.messages = [
        {'role':'system', 'content':system_prompt}
    ]

# Display Chat History
for msg in st.session_state.messages:
    if msg['role'] != 'system':
        with st.chat_message(msg['role']):
            st.markdown(msg['content'])

# Chat Input
user_input = st.chat_input('Ask you query related to Data Science...')

if user_input:
    # Store user message
    st.session_state.messages.append(
        {"role": "user", "content": user_input}
    )

    with st.chat_message("user"):
        st.markdown(user_input)

    with st.spinner("Thinking..."):

        # Recreate chat session each run
        chat = client.chats.create(
            model="gemini-2.5-flash",
            config={
                "system_instruction": system_prompt
            }
        )

        # Replay previous conversation (except system)
        for msg in st.session_state.messages[:-1]:
            if msg["role"] != "system":
                chat.send_message(msg["content"])

        # Send latest user message
        response = chat.send_message(user_input)
        bot_reply = response.text

    # Store assistant reply
    st.session_state.messages.append(
        {"role": "assistant", "content": bot_reply}
    )

    with st.chat_message("assistant"):
        st.markdown(bot_reply)