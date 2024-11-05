import streamlit as st
from openai import OpenAI

# Initialize OpenAI client with API key from Streamlit secrets
api_key = st.secrets["open_api_key]
client = OpenAI(api_key=api_key)

def main():
    st.title("OpenAI Chat Test")
    user_input = st.text_input("Ask OpenAI something:")

    if user_input:
        try:
            response = client.chat.completions.create(
                model="gpt-3.5-turbo",
                messages=[{"role": "user", "content": user_input}]
            )
            st.write(response.choices[0].message['content'])
        except Exception as e:
            st.error(f"Error: {e}")

if __name__ == "__main__":
    main()

