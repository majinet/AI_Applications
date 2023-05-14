import openai

def create_bdd():
    openai.api_key = ""

    with open('../../bus_requirements/calculator.func', 'r') as file:
        file_content = file.read()

    print(file_content)

    prompt = f"Write cucumber BDD with data from function requirements ---{file_content}---"

    # Get a response from GPT-3
    completion = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "user", "content": prompt}
        ],
        n=1,
    )

    # Get the summary from the response
    content = completion.choices[0].message["content"]

    print(content)

    with open("../../features/calculator.feature", "w") as outfile:
        outfile.write(content)

if __name__ == '__main__':
    create_bdd()