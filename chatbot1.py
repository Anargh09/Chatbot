import streamlit as st

# Simple chatbot response function


def get_bot_response(user_message):
    user_message = user_message.lower().strip()
    if not user_message:
        return "Please type something!"
    elif "hello" in user_message or "hi" in user_message:
        return "Hello! How can I help you today?"
    elif "weather" in user_message:
        return "I'm not connected to real-time data, but it's always sunny in code!"
    elif "bye" in user_message or "goodbye" in user_message:
        return "Goodbye! Have a great day."
    elif "name" in user_message:
        return "I'm a simple chatbot built with Streamlit. What's your name?"
    else:
        return "I'm a basic bot. Try saying 'hello', 'weather', or 'bye' for a response!"


# Streamlit app setup
st.title("Working Chatbot")
st.write("Type your message below and click 'Send' to chat. The bot will reply!")

# Initialize chat history if not already done
if "chat_history" not in st.session_state:
    st.session_state.chat_history = []

# Display chat history
st.subheader("Chat History")
chat_container = st.container()
with chat_container:
    for message in st.session_state.chat_history:
        if message["role"] == "user":
            st.write(f"**You:** {message['text']}")
        else:
            st.write(f"**Bot:** {message['text']}")

# Use a form for input to allow clearing
with st.form(key="chat_form"):
    user_input = st.text_input("Your message:", placeholder="Type here...")
    submit_button = st.form_submit_button("Send")

    if submit_button and user_input:
        # Add user message to history
        st.session_state.chat_history.append(
            {"role": "user", "text": user_input})

        # Get and add bot response
        bot_reply = get_bot_response(user_input)
        st.session_state.chat_history.append(
            {"role": "bot", "text": bot_reply})

        # Rerun the app to update the display
        st.rerun()
    elif submit_button and not user_input:
        st.warning("Please enter a message before sending.")
