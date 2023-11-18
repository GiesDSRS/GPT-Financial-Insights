import streamlit as st
import os
import openai
import time

# OpenAI API configuration details
openai.api_type = "azure"
openai.api_base = "https://dsrsllm.openai.azure.com/"
openai.api_version = "2023-07-01-preview"
openai.api_key = os.environ['OPENAI_API_KEY']
dsrs_engine = "test32"  # Use test32 for chat-gpt-4-32k

# Define the max token limit for the OpenAI API (including both prompt and completion)
MAX_TOKEN_LIMIT = 4096


# Function to interact with the OpenAI API with rate limit handling
def chat_with_gpt(prompt):
    prompt2 = [{"role":"user","content": prompt}]
    try:
        response = openai.ChatCompletion.create(
            engine=dsrs_engine,
            messages=prompt2,
            max_tokens=MAX_TOKEN_LIMIT,
            temperature=0,
            top_p=0.95,
            frequency_penalty=0,
            presence_penalty=0,
            stop=None
        )
        print(response)
        return response.choices[0].message.content
    except Exception as e:
        st.error(f"An error occurred: {e}")
        time.sleep(2)  # Wait 2 seconds before retrying


# Function to read content from a file and split into manageable chunks
def doc_content(filename):
    with open(filename, 'r') as file:
        content = file.read()
    return content


# Function to split content based on full stops (.) to maintain context
def split_content(content, max_length):
    sentences = content.split('.')
    chunks = []
    current_chunk = ''

    for sentence in sentences:
        if len(current_chunk) + len(sentence) < max_length and sentence:
            current_chunk += sentence + '.'
        else:
            chunks.append(current_chunk)
            current_chunk = sentence + '.'
    if current_chunk:
        chunks.append(current_chunk)
    return chunks


# Streamlit app function
def streamlit_app():
    st.title("OpenAI GPT Analysis Interface")

    # Text input for the text file path
    file_path = st.text_input("Enter the path to your text file")

    # Text area for user to enter their question
    question = st.text_area("Enter your question for the AI")

    # Button to run the analysis
    if st.button("Run Analysis"):
        if os.path.exists(file_path) and os.path.isfile(file_path):
            content = doc_content(file_path)  # Get the content of the file
            chunks = split_content(content, MAX_TOKEN_LIMIT * 4)  # Estimate the number of characters per token
            combined_responses = []

            with st.spinner('Processing...'):
                for i, chunk in enumerate(chunks):
                    st.write(f"Processing chunk {i + 1}/{len(chunks)}...")
                    response = chat_with_gpt(chunk + "\n\n" + question)
                    combined_responses.append(response)
                    time.sleep(1)  # Throttle requests to avoid rate limiting

                # After all chunks are processed, combine responses and display
                full_analysis = ' '.join(combined_responses)
                st.text_area("Analysis Result", full_analysis, height=300)
        else:
            st.error(f"The file {file_path} does not exist.")


if __name__ == "__main__":
    streamlit_app()
