import os
import openai
import streamlit as st

# Load environment variables from .env file
# Set up OpenAI API Key
openai.api_key = ("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")

def generate_linkedin_post(prompt: str) -> str:
    """Generate a LinkedIn post based on the user's prompt using OpenAI."""

    response = openai.ChatCompletion.create(
        model="ft:gpt-3.5-turbo-0613:matt-young-media::7t3Iz7tA",
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
    return assistant_response

# Streamlit UI
st.title("LinkedIn Post Generator Assistant")

# Initial conversation
st.write("AI: Hi! Let's create a LinkedIn post. What's the main topic or achievement you'd like to share?")
topic = st.text_input("You:")

if topic:
    detail_prompt = f"Can you provide more details about {topic}?"
    st.write(f"AI: {detail_prompt}")
    detail = st.text_input("You (Detail about the topic):")

    if detail:
        initial_prompt = f"I want to share about {topic}. {detail}"
        post = generate_linkedin_post(initial_prompt)

        st.write(f"AI: Here's your LinkedIn post based on your input:")
        st.text_area("Generated LinkedIn Post:", post)

        st.write("AI: How would you like to modify or refine the post?")
        feedback = st.text_input("You (Feedback on the post):")

        if feedback:
            revised_prompt = f"{initial_prompt}. However, {feedback}"
            revised_post = generate_linkedin_post(revised_prompt)
            st.write(f"AI: Based on your feedback, here's the revised post:")
            st.text_area("Revised LinkedIn Post:", revised_post)
            st.write("AI: Feel free to provide more feedback or post it directly on LinkedIn!")
