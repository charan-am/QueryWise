
import streamlit as st
from main import get_answer, knowledge_base


# ==========================================
# 1. PAGE CONFIGURATION
# ==========================================

st.set_page_config(
    page_title="QueryWise - Developer Assistant",
    page_icon="🧠",
    layout="centered"
)


# ==========================================
# 2. SIDEBAR
# ==========================================

with st.sidebar:

    st.title("🧠 QueryWise")

    st.caption("Your Intelligent Developer Knowledge Assistant")

    st.divider()

    st.subheader("Knowledge Base")

    st.metric(
        "Available FAQ Entries",
        len(knowledge_base)
    )

    st.divider()

    st.subheader("Try asking")

    example_questions = [
        "What is Python?",
        "What is a Python list?",
        "How does Git work?",
        "What is AI?",
        "What is Machine Learning?",
        "What is overfitting?"
    ]

    for question in example_questions:
        st.markdown(f"- {question}")

    st.divider()

    if st.button("🗑️ Clear Conversation", use_container_width=True):

        st.session_state.messages = []
        st.rerun()

    st.caption("Powered by Python, Scikit-learn and TF-IDF")


# ==========================================
# 3. MAIN APPLICATION HEADER
# ==========================================

st.title("💬 QueryWise")

st.markdown(
    "Ask questions about **Python, Git, GitHub, "
    "VS Code and Machine Learning.**"
)

st.caption(
    "An NLP-powered developer knowledge assistant."
)

st.divider()


# ==========================================
# 4. INITIALIZE CHAT HISTORY
# ==========================================

if "messages" not in st.session_state:

    st.session_state.messages = []


# ==========================================
# 5. DISPLAY PREVIOUS CONVERSATION
# ==========================================

for message in st.session_state.messages:

    with st.chat_message(message["role"]):

        st.markdown(message["content"])

        if message["role"] == "assistant":

            if message.get("matched_question"):

                with st.expander("View retrieval details"):

                    st.write(
                        "**Matched FAQ:**",
                        message["matched_question"]
                    )

                    st.metric(
                        "Similarity Score",
                        f"{message['score']:.2f}"
                    )

                    st.caption(
                        "Similarity is a mathematical retrieval "
                        "score, not a probability of correctness."
                    )

            elif message.get("no_match"):

                with st.expander("View retrieval details"):

                    st.write("No sufficiently relevant FAQ was found.")

                    st.metric(
                        "Best Similarity Score",
                        f"{message['score']:.2f}"
                    )


# ==========================================
# 6. USER CHAT INPUT
# ==========================================

user_question = st.chat_input(
    "Ask QueryWise a developer question..."
)


# ==========================================
# 7. PROCESS USER QUESTION
# ==========================================

if user_question:

    # Save the user's message
    st.session_state.messages.append(
        {
            "role": "user",
            "content": user_question
        }
    )

    # Retrieve the answer using our NLP engine
    answer, score, matched_question = get_answer(
        user_question
    )

    # Handle insufficient information
    if answer is None:

        response = (
            "I couldn't find sufficiently relevant information "
            "in my knowledge base. Try asking something about "
            "Python, Git, VS Code or Machine Learning."
        )

        assistant_message = {
            "role": "assistant",
            "content": response,
            "score": score,
            "no_match": True
        }

    else:

        assistant_message = {
            "role": "assistant",
            "content": answer,
            "score": score,
            "matched_question": matched_question
        }

    # Save the assistant's response
    st.session_state.messages.append(assistant_message)

    # Refresh the page to display the complete conversation
    st.rerun()
