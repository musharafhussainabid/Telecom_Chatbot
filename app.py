import streamlit as st
from chatbot_engine import get_chat_response

st.set_page_config(page_title="Telecom Support Chatbot", layout="centered")

st.title("Telecom Support Chatbot")
st.markdown("Ask me anything related to telecom support — plans, connectivity, devices, and more!")

# Initialize chat history in session state
if "chat_history" not in st.session_state:
    st.session_state.chat_history = []

# Text input for user query
user_input = st.text_input("Type your question here:", key="user_input")

# Process input and get response
if user_input:
    response = get_chat_response(user_input)  

    # Save conversation to session state
    st.session_state.chat_history.append(("user", user_input))
    st.session_state.chat_history.append(("bot", response))

# Display chat history
for role, msg in st.session_state.chat_history:
    if role == "user":
        st.markdown(f" **You:** {msg}", unsafe_allow_html=True)
    else:
        st.markdown(f" **Bot:** {msg}", unsafe_allow_html=True)
