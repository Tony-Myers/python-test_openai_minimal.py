import streamlit as st
from openai import OpenAI

# Initialize OpenAI client with API key from Streamlit secrets
try:
    # Correctly retrieve the API key with the exact name
    api_key = st.secrets["OPENAI_API_KEY"]
    client = OpenAI(api_key=api_key)
except KeyError:
    st.error("OpenAI API key not found. Please add it to Streamlit secrets.")
    st.stop()

def main():
    st.title("OpenAI Chat Test")
    user_input = st.text_input("Ask OpenAI something:")

    if user_input:
        try:
            response = client.chat.completions.create(
                model="gpt-3.5-turbo",
                messages=[{"role": "user", "content": user_input}]
            )
            # Correctly access the content of the response message
            message_content = response.choices[0].message.content
            st.write(message_content)
        except Exception as e:
            st.error(f"Error: {e}")

if __name__ == "__main__":
    main()




