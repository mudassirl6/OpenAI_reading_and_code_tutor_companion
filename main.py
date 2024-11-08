import openai
import streamlit as st
import json
import os
from dotenv import load_dotenv

load_dotenv()
# Set up OpenAI API Key
# Load environment variables from .env file

# Access the OpenAI API key from environment variables
openai.api_key = os.getenv("openai_key")


# Function to get a summary of the passage (Reading Companion)
def get_summary(text, max_tokens=50):
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",  # Using gpt-3.5-turbo
        messages=[
            {"role": "system", "content": "You are a helpful assistant."},
            {"role": "user", "content": f"Summarize the following text:\n\n{text}"}
        ],
        max_tokens=max_tokens
    )
    summary = response['choices'][0]['message']['content'].strip()
    return summary

# Function to provide context or background on the passage (Reading Companion)
def get_context(text, max_tokens=100):
    response = openai.chat_completions.create(
        model="gpt-3.5-turbo",  # Using gpt-3.5-turbo
        messages=[
            {"role": "system", "content": "You are a helpful assistant."},
            {"role": "user", "content": f"Provide additional context or background information for the following text:\n\n{text}"}
        ],
        max_tokens=max_tokens
    )
    context = response['choices'][0]['message']['content'].strip()
    return context

# Function to explain difficult passages in simple terms (Reading Companion)
def explain_passage(text, max_tokens=100):
    response = openai.chat_completions.create(
        model="gpt-3.5-turbo",  # Using gpt-3.5-turbo
        messages=[
            {"role": "system", "content": "You are a helpful assistant."},
            {"role": "user", "content": f"Explain the following text in simple terms:\n\n{text}"}
        ],
        max_tokens=max_tokens
    )
    explanation = response['choices'][0]['message']['content'].strip()
    return explanation

# Function to get coding hints (Virtual Tutor)
def get_coding_hint(code_snippet):
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",  # Using gpt-3.5-turbo
        messages=[
            {"role": "system", "content": "You are a helpful coding tutor."},
            {"role": "user", "content": f"Provide helpful hints for solving this coding problem:\n\n{code_snippet}"}
        ],
        max_tokens=100
    )
    hint = response['choices'][0]['message']['content'].strip()
    return hint

# Function to explain code (Virtual Tutor)
def explain_code(code_snippet):
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",  # Using gpt-3.5-turbo
        messages=[
            {"role": "system", "content": "You are a helpful coding tutor."},
            {"role": "user", "content": f"Explain the following code snippet in simple terms:\n\n{code_snippet}"}
        ],
        max_tokens=100
    )
    explanation = response['choices'][0]['message']['content'].strip()
    return explanation

# Progress tracker (Saving session history in a local file)
def track_progress(user_input, output, file_path="progress.json"):
    if os.path.exists(file_path):
        with open(file_path, "r") as file:
            progress_data = json.load(file)
    else:
        progress_data = []
    
    progress_data.append({"input": user_input, "output": output})
    
    with open(file_path, "w") as file:
        json.dump(progress_data, file)

# Streamlit UI
def main():
    st.title("Virtual Tutor for Coding Practice and Personalized Reading Companion 📚💻")
    
    st.sidebar.title("Navigation")
    option = st.sidebar.radio("Choose a mode:", ["Reading Companion", "Virtual Coding Tutor"])

    if option == "Reading Companion":
        # Text input for user to paste a passage
        text = st.text_area("Enter the passage you'd like help with:")

        # Display the number of tokens in the text
        if text:
            token_count = len(text.split())
            st.write(f"Your text contains {token_count} tokens.")

        # Add a slider for controlling the max tokens in the response
        max_tokens = st.slider("Max Tokens for Responses", min_value=30, max_value=200, value=100)

        # Buttons for each action
        if st.button("Get Summary"):
            if text:
                with st.spinner("Generating summary..."):
                    summary = get_summary(text, max_tokens=max_tokens)
                st.subheader("Summary:")
                st.write(summary)
            else:
                st.warning("Please enter some text to summarize.")

        if st.button("Get Context"):
            if text:
                with st.spinner("Fetching context..."):
                    context = get_context(text, max_tokens=max_tokens)
                st.subheader("Context:")
                st.write(context)
            else:
                st.warning("Please enter some text to get context.")

        if st.button("Explain in Simple Terms"):
            if text:
                with st.spinner("Explaining..."):
                    explanation = explain_passage(text, max_tokens=max_tokens)
                st.subheader("Explanation:")
                st.write(explanation)
            else:
                st.warning("Please enter some text to get an explanation.")

    elif option == "Virtual Coding Tutor":
        # Code input for the coding tutor
        code = st.text_area("Enter your code or coding challenge:")

        # Provide coding hints and explanations
        if st.button("Get Coding Hint"):
            if code:
                with st.spinner("Generating hint..."):
                    hint = get_coding_hint(code)
                st.subheader("Coding Hint:")
                st.write(hint)
                track_progress(code, hint)
            else:
                st.warning("Please enter some code to get a hint.")

        if st.button("Explain Code"):
            if code:
                with st.spinner("Explaining code..."):
                    explanation = explain_code(code)
                st.subheader("Code Explanation:")
                st.write(explanation)
                track_progress(code, explanation)
            else:
                st.warning("Please enter some code to get an explanation.")

if __name__ == "__main__":
    main()