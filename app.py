import streamlit as st
from hugchat import hugchat
from hugchat.login import Login
import os
import json

# App title
st.title('Enhanced ChatBot')

# Sidebar for Hugging Face Credentials
with st.sidebar:
    st.title('Login HugChat')
    hf_email = st.text_input('Enter E-mail:')
    hf_pass = st.text_input('Enter Password:', type='password')
    if not (hf_email and hf_pass):
        st.warning('Please enter your account!', icon='⚠️')
    else:
        st.success('Proceed to entering your prompt message!', icon='👉')

    # Multiple Chatbots
    st.title('Select ChatBot Model')
    model_choice = st.selectbox('Choose a model:', [
        'C4AI',
        'Meta-Llama',
        'Zephyr-orpo',
        'Mixtral-8x7B',
        'Nous-Hermes-2',
        'Yi-1.5-34B',
        'Gemma-1.1',
        'Mistral-7B',
        'Phi-3'
    ])

    # Session Management
    st.title('Manage Session')
    save_session = st.button('Save Session')
    load_session = st.button('Load Session')
    clear_session = st.button('Clear Chat History')


# Session management functions
def save_chat_session():
    try:
        with open('chat_session.json', 'w') as f:
            json.dump(st.session_state.messages, f)
        st.success('Session saved!')
    except Exception as e:
        st.error(f"An error occurred while saving the session: {e}")


def load_chat_session():
    try:
        if os.path.exists('chat_session.json'):
            with open('chat_session.json', 'r') as f:
                st.session_state.messages = json.load(f)
            st.success('Session loaded!')
        else:
            st.warning('No saved session found.')
    except Exception as e:
        st.error(f"An error occurred while loading the session: {e}")


def clear_chat_history():
    st.session_state.messages = [{"role": "assistant", "content": "How may I help you?"}]
    st.success('Chat history cleared!')


# Handle session management actions
if save_session:
    save_chat_session()
if load_session:
    load_chat_session()
if clear_session:
    clear_chat_history()

# Ensure session state is initialized
if "messages" not in st.session_state:
    st.session_state.messages = [{"role": "assistant", "content": "How may I help you?"}]

# Display chat messages
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.write(message["content"])


# Function for generating LLM response
def generate_response(prompt_input, email, passwd, model_choice):
    # Hugging Face Login
    sign = Login(email, passwd)
    cookies = sign.login()

    # Choose the model based on user selection
    model_mapping = {
        'C4AI': 0,
        'Meta-Llama': 1,
        'Zephyr-orpo': 2,
        'Mixtral-8x7B': 3,
        'Nous-Hermes-2': 4,
        'Yi-1.5-34B': 5,
        'Gemma-1.1': 6,
        'Mistral-7B': 7,
        'Phi-3': 8
    }
    model = model_mapping.get(model_choice)

    # Create ChatBot with the chosen model
    chatbot = hugchat.ChatBot(cookies=cookies.get_dict(), default_llm=model)
    return chatbot.chat(prompt_input)


# User-provided prompt
if prompt := st.chat_input(disabled=not (hf_email and hf_pass)):
    st.session_state.messages.append({"role": "user", "content": prompt})
    with st.chat_message("user"):
        st.write(prompt)

# Generate a new response if last message is not from assistant
if st.session_state.messages[-1]["role"] != "assistant":
    with st.chat_message("assistant"):
        with st.spinner("Thinking..."):
            response = generate_response(prompt, hf_email, hf_pass, model_choice)
            st.write(response)
    message = {"role": "assistant", "content": response.text}
    st.session_state.messages.append(message)
