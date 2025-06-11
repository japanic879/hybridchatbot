import streamlit as st
import os
from datetime import datetime
from chatbot_module import ExcelSchoolChatbot, generate_excel_template  # move your original classes/functions here

# ---------- Setup ----------
TEMPLATE_PATH = 'school_chatbot_template.xlsx'
if not os.path.exists(TEMPLATE_PATH):
    generate_excel_template(TEMPLATE_PATH)

@st.cache_resource
def load_chatbot():
    return ExcelSchoolChatbot(TEMPLATE_PATH)

bot = load_chatbot()

# ---------- Streamlit UI ----------
st.set_page_config(page_title="School Chatbot", layout="wide")
st.title("🎓 School Info Chatbot")
st.markdown("Ask any question about the school, such as schedules, staff, or admissions.")

# User Type Selector
user_type = st.radio("You are a:", ["guest", "student", "parent"], horizontal=True)

# Chat input/output
query = st.text_input("Your question", placeholder="e.g., What are the school fees?")
if st.button("Ask") or query:
    if query.strip():
        response = bot.get_response(query, user_type)
        st.success(response)
    else:
        st.warning("Please enter a question.")

# Optional: Display FAQ examples
with st.expander("💡 Sample Questions"):
    st.write("- What are the admission requirements?")
    st.write("- Is there a school bus service?")
    st.write("- Who is the principal?")
    st.write("- What is the morning schedule?")
