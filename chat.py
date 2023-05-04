
import os

import replicate
import streamlit as st
from dotenv import load_dotenv
from elevenlabs import generate
from langchain import PromptTemplate
from langchain.chains import LLMChain
from langchain.llms import OpenAI

load_dotenv()

openai_api_key = os.getenv("OPENAI_API_KEY")
eleven_api_key = os.getenv("ELEVEN_API_KEY")

llm = OpenAI(temperature=0.9)

def generate_story(text):
    """Generate a story using the langchain library and OpenAI's GPT-3 model."""
    prompt = PromptTemplate(
        input_variables=["text"],
        template=""" 
         You are a fun and seasoned storyteller. Generate a story for me about {text}.
                 """
    )
    story = LLMChain(llm=llm, prompt=prompt)
    return story.run(text=text)


def generate_audio(text, voice):
    """Convert the generated story to audio using the Eleven Labs API."""
    audio = generate(text=text, voice=voice, api_key=eleven_api_key)
    return audio


def generate_images(story_text):
    """Generate images using the story text using the Replicate API."""
    output = replicate.run(
        "stability-ai/stable-diffusion:db21e45d3f7023abc2a46ee38a23973f6dce16bb082a930b0c49861f96d1e5bf",
        input={"prompt": story_text}
    )
    return output


def app():
    st.title("Story Storm")

    with st.form(key='my_form'):
        text = st.text_input(
            "Enter a word to generate a story",
            max_chars=None,
            type="default",
            placeholder="Enter a word to generate a story",
        )
        options = ["Bella", "Antoni", "Arnold", "Adam", "Domi", "Elli", "Josh", "Rachel", "Sam"]
        voice = st.selectbox("Select a voice", options)

        if st.form_submit_button("Submit"):
            with st.spinner('Generating story...'):
                story_text = generate_story(text)
                audio = generate_audio(story_text, voice)

            st.audio(audio, format='audio/mp3')
            images = generate_images(story_text)
            for item in images:
                st.image(item)

    if not text or not voice:
        st.info("Please enter a word and select a voice")


if __name__ == '__main__':
    app()