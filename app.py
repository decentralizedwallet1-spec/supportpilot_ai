

import streamlit as st

st.set_page_config(
    page_title="SupportPilot AI",
    page_icon="🤖"
)

# Business knowledge
faqs = {
    "opening hours":
        "We are open Monday to Saturday, 9 AM to 6 PM.",

    "delivery":
        "Delivery usually takes 2 to 5 business days.",

    "payment":
        "We accept bank transfers and card payments.",

    "contact":
        "You can contact our support team by email."
}

def get_response(question):
    question = question.lower()

    for keyword, answer in faqs.items():
        if keyword in question:
            return answer

    return (
        "I don't have enough information "
        "to answer that question. "
        "Please contact a human support agent."
    )

st.title("🤖 SupportPilot AI")
st.write("Your intelligent customer support assistant.")

if "messages" not in st.session_state:
    st.session_state.messages = []

for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.write(message["content"])

question = st.chat_input("Ask us a question...")

if question:
    st.session_state.messages.append({
        "role": "user",
        "content": question
    })

    answer = get_response(question)

    st.session_state.messages.append({
        "role": "assistant",
        "content": answer
    })

    st.rerun()
