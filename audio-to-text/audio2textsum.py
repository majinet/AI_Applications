from fastapi import FastAPI, File, Form, HTTPException, UploadFile, Header
import requests
import os
import openai

app = FastAPI()

@app.post("/transcribe_audio")
async def transcribe_audio(file: UploadFile = File(...)):
    """
    Transcribe audio using the OpenAI API and return the transcript.
    """

    openai.api_key = ""
    audio_file = open(f"audio/{file.filename}", "rb")
    transcript = openai.Audio.transcribe("whisper-1", audio_file)

    print(transcript)

    #Define the prompt for GPT-3

    prompt = f"summarize the text into about 50 words '''{transcript}'''"

    # Get a response from GPT-3
    completion = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "user", "content": prompt}
        ],
        n=1,
    )

    # Get the summary from the response
    summary = completion.choices[0].message

    # Print the summary

    print(f"Summary: {summary}")

    return summary
