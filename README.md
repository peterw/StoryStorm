# Story Storm
We got a treat for you! Introducing Story Storm, a powerful tool that harnesses the power of OpenAI's GPT-3.5 Turbo API to generate fascinating and engaging stories.
But we didn't stop there! We wanted to make your story experience even more immersive. That's why we've also integrated the Eleven Labs API to convert your generated story into an audio narration.
And that's not all! We've also incorporated the replicate API to generate accompanying images for your story. So now, as you listen, you can also see vivid depictions of the story's characters and settings.

## Getting Started
To get started, clone the repository and install the required dependencies:


```git clone https://github.com/your-username/story-storm.git```

```cd Story_storm```

```pip install -r requirements.txt```

## Prerequisites
You will need to set up API keys for[OpenAI](https://platform.openai.com/account/api-keys),[Eleven Labs ](https://beta.elevenlabs.io/speech-synthesis) [Replicate](https://replicate.com/account/api-tokens). 

### Windows
```setx OPENAI_API_KEY <your_openai_api_key>```

```setx ELEVEN_API_KEY <your_eleven_labs_api_key>```

```setx REPLICATE_API_KEY <your_replicate_api_key>```
### Linux and Mac
```export OPENAI_API_KEY=<your_openai_api_key>```

```export ELEVEN_API_KEY=<your_eleven_labs_api_key>```

```export REPLICATE_API_KEY=<your_replicate_api_key>```

## Usage
To run the program, simply run the following command in the terminal:

```streamlit run main.py --server.port 8080```

Then enter a word and select a voice to generate a story.

## Credits
This project uses the following libraries:

1. langchain
2. streamlit
3. dotenv
4. elevenlabs
5. replicate

## License
This project is licensed under the MIT License - see the LICENSE file for details.