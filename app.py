import streamlit as st
import openai

# Load API key from Streamlit secrets
openai.api_key = st.secrets["OPENAI_API_KEY"]

# Create an OpenAI client
client = openai.OpenAI()

# Streamlit UI setup
st.set_page_config(page_title="CC BI Days Assistant", layout="wide")

# Sidebar with additional information
with st.sidebar:
    st.header("📌 CC BI Days Assistant")
    st.markdown("🤖 **Your AI-powered assistant for CC BI Days.**")
    st.markdown("💡 Ask questions about BI, data insights, and analytics.")
    
    st.divider()

    st.subheader("🔗 Useful Links")
    st.markdown("[📘 OpenAI Docs](https://platform.openai.com/docs/)")
    st.markdown("[💬 Streamlit Docs](https://docs.streamlit.io/)")
    st.markdown("[🌐 Company Website](https://www.camelot-mc.com/)")

    st.divider()

    st.subheader("📞 Contact")
    st.markdown("👤 **Your Name**")
    st.markdown("✉️ [your.email@example.com](mailto:your.email@example.com)")
    st.markdown("📍 Location: Kehl, Germany")

    st.divider()

    st.markdown("🛠️ Developed by **Muhammad Ali Zia** 🚀")

# Main title
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
