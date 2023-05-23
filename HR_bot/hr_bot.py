from fastapi import FastAPI, File, Form, HTTPException, UploadFile, Header
import requests
import os
import openai

app = FastAPI()


@app.post("/hr_bot")
async def hr_bot(file: UploadFile = File(...)):
    """
    Transcribe audio using the OpenAI API and return the transcript.
    """

    openai.api_key = ""
    transcript = open(f"transcript/{file.filename}", "rb")

    print(transcript)

    #Define the prompt for GPT-3

    prompt = f"Assume you are a HR to select talent person. After you read this cover letter '''{transcript}''', will you give me a chance to interview? if refuse, give me reason why I'm not the right person for selection."

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
