import streamlit as st
import datetime

st.set_page_config(page_title="Friendly Chatbot", page_icon="💬")
st.title("💬 Talk to Your Friendly Chatbot!")
st.markdown("Let's have a fun chat 😄")

if "chat_history" not in st.session_state:
    st.session_state.chat_history = []

def chatbot_reply(user_input):
    user_input = user_input.lower()

    if "hello" in user_input or "hi" in user_input:
        return "Hey there! 😊 How's your day going?"
    elif "how are you" in user_input:
        return "I'm just a bot, but I'm doing great! How about you?"
    elif "good" in user_input or "fine" in user_input:
        return "Awesome! Glad to hear that! 🌟"
    elif "sad" in user_input or "not good" in user_input:
        return "I'm here for you 💙 Want to talk about it?"
    elif "time" in user_input:
        now = datetime.datetime.now()
        return f"The current time is {now.strftime('%I:%M %p')}"
    elif "your name" in user_input:
        return "I'm your virtual buddy 🤖 You can name me anything you like!"
    elif "bye" in user_input or "see you" in user_input:
        return "Bye! Take care 🫶 Come back if you feel like chatting!"
    else:
        return "Hmm... I didn't get that. But I'm listening! 🧠💭"

user_input = st.text_input("You:", key="input")

if st.button("Send"):
    if user_input:
        reply = chatbot_reply(user_input)
        st.session_state.chat_history.append(("You", user_input))
        st.session_state.chat_history.append(("Bot", reply))


for sender, message in st.session_state.chat_history:
    if sender == "You":
        st.markdown(f"**🧍 You:** {message}")
    else:
        st.markdown(f"**🤖 Bot:** {message}")
