import openai

def create_python():
    openai.api_key = ""

    with open('../../features/calculator.feature', 'r') as file:
        file_content = file.read()

    print(file_content)

    prompt = f"Create py code only follow best practice, PEP8 and docstring from cucumber bdd without test functions: ---{file_content}---"

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

    with open("../../py/calculator.py", "w") as outfile:
        outfile.write(content)


if __name__ == '__main__':
    create_python()