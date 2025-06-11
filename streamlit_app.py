import streamlit as st
from ExcelSchoolChatbot import ExcelSchoolChatbot, generate_excel_template
import os

EXCEL_PATH = "school_chatbot_template.xlsx"
if not os.path.exists(EXCEL_PATH):
  generate_excel_template(EXCEL_PATH)

if "chatbot" not in st.session_state:
  st.session_state.chatbot = ExcelSchoolChatbot(EXCEL_PATH)

chatbot = st.session_state.chatbot
st.title("School Info Chatbot")

user_type = st.sidebar.radio("I am a...", ["guest", "parent", "student"])
user_input = st.text_input("Ask your question below:")

if "chat_history" not in st.session_state:
  st.session_state.chat_history = []

if user_input:
  response = chatbot.get_response(user_input, user_type)
  st.session_state.chat_history.append(("You", user_input))
  st.session_state.chat_history.append(("Bot", response))

for sender, message in st.session_state.chat_history:
  if sender == "You":
    st.markdown(f"** {sender}**: {message}")
  else:
    st.markdown(f"** {sender}**: {message}")
