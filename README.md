# Simple Chatbot

Simple ChatBot is a Streamlit application that allows users to interact with various chat models provided by Hugging Face. 
The app supports user authentication, model selection, and session management.

## Features

- User authentication using Hugging Face credentials.
- Selection of multiple chat models.
- Session management (save, load, and clear chat history).
- Display of chat messages between the user and the chatbot.

## Installation

1. **Clone the repository:**
    ```bash
    git clone https://github.com/tom1209-netizen/simple-chatbot.git
    cd simple-chatbot
    ```

2. **Create a virtual environment and activate it:**
    ```bash
    python -m venv venv
    source venv/bin/activate 
    ```

3. **Install the required dependencies:**
    ```bash
    pip install -r requirements.txt
    ```

4. **Run the application:**
    ```bash
    streamlit run app.py
    ```

## Usage

1. **Login:**
   - Enter your Hugging Face email and password in the sidebar to authenticate.

2. **Select ChatBot Model:**
   - Choose a model from the dropdown menu in the sidebar.
   - The following models are available:
     - C4AI
     - Meta-Llama
     - Zephyr-orpo
     - Mixtral-8x7B
     - Nous-Hermes-2
     - Yi-1.5-34B
     - Gemma-1.1
     - Mistral-7B
     - Phi-3

3. **Manage Session:**
    - Use the buttons to save, load, or clear the chat history.

4. **Interact with the ChatBot:**
    - Type your message in the input box at the bottom of the page and press Enter to send it.

## Session Management

- **Save Session:** Saves the current chat history to a JSON file (`chat_session.json`).
- **Load Session:** Loads the chat history from the JSON file.
- **Clear Chat History:** Clears the current chat history.