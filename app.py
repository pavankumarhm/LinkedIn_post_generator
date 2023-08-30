import os
import openai
import streamlit as st
from dotenv import load_dotenv

# Setup OpenAI key and Model from secrets
openai.api_key = st.secrets["open_ai_key"]
MODEL = st.secrets["MODEL"]

# Streamlit configurations
st.set_page_config(
    page_title="LinkedIn Post Generator Assistant",
    layout="centered",
    initial_sidebar_state="collapsed",
)

def generate_linkedin_post(prompt: str) -> str:
    try:
        response = openai.ChatCompletion.create(
            model= MODEL,
            messages=[
                {
                    "role": "user",
                    "content": prompt
                }
            ],
            temperature=0.5,
            top_p=1,
            frequency_penalty=0,
            presence_penalty=0
        )
        assistant_response = response['choices'][0]['message']['content']
    except Exception as e:
        st.error(f"Error: {str(e)}")
        return "An error occurred while generating the post."
    return assistant_response

# Main App UI
st.image("linkedin-bot-automation-tool.png", use_column_width="auto")  # Add a cool image on top (e.g., AI, robot)
st.title("🤖 **LinkedIn Post Generator Assistant**")
st.write("Let's create an intriguing LinkedIn post! 🚀")

# Input from user
topic = st.text_input("👩‍💼 **You**: What's the main topic or achievement you'd like to share?")

if topic:
    st.write(f"🤖 **AI**: Add some details about the *{topic}* to make it more intriguing.")
    detail = st.text_input("👩‍💼 **You**: Details about the topic")

    if detail:
        initial_prompt = f"Write an intriguing LinkedIn post using {topic} and {detail}. add some emojis when needed"
        post = generate_linkedin_post(initial_prompt)
        st.write(f"🤖 **AI**: Here's your LinkedIn post:")
        st.text_area("", post, height=200)

        feedback = st.text_input("👩‍💼 **You**: How would you like to modify or refine the post?")

        if feedback:
            revised_prompt = f"Modify the post: '{post}' with feedback: '{feedback}'"
            revised_post = generate_linkedin_post(revised_prompt)
            st.write(f"🤖 **AI**: Based on your feedback, here's the revised post:")
            st.text_area("", revised_post, height=200)
            st.write("🤖 **AI**: Feel free to provide more feedback or post it directly on LinkedIn!")

# Custom CSS for enhancing the look
st.markdown(
    """
    <style>
        body {
            color: #4f8bf9;
            background-color: #f4f4f9;
        }
        .stTextInput>div>div>input {
            padding: 10px 15px;
            border-radius: 5px;
            border: 1px solid #4f8bf9;
        }
        textarea {
            padding: 10px 15px !important;
        }
    </style>
    """,
    unsafe_allow_html=True,
)
