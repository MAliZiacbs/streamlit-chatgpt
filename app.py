import streamlit as st
import openai

# Load API key from Streamlit secrets
openai.api_key = st.secrets["OPENAI_API_KEY"]

# Create an OpenAI client
client = openai.OpenAI()


st.markdown(
    """
    <style>
        body {
            background-color: #FFA500; /* Orange */
        }
        .stApp {
            background-color: #FFA500;
        }
        .stChatMessage {
            border-radius: 10px;
            padding: 10px;
        }
    </style>
    """,
    unsafe_allow_html=True
)


# Streamlit UI setup
st.set_page_config(page_title="CC BI Days Assistant", layout="centered")

st.title("💬 CC BI Days Assistant")
st.markdown("Ask any question and get an AI-generated response.")

# Store chat history
if "messages" not in st.session_state:
    st.session_state.messages = []

# Display previous chat messages
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

# Input box for user message
if prompt := st.chat_input("Type your question here..."):
    # Add user message to chat history
    st.session_state.messages.append({"role": "user", "content": prompt})

    with st.chat_message("user"):
        st.markdown(prompt)

    # Call OpenAI API with the new syntax
    response = client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=[{"role": m["role"], "content": m["content"]} for m in st.session_state.messages]
    )

    reply = response.choices[0].message.content  # New way to access response

    # Add assistant's response to chat history
    st.session_state.messages.append({"role": "assistant", "content": reply})

    with st.chat_message("assistant"):
        st.markdown(reply)
