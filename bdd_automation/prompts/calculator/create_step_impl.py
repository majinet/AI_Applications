import openai

def create_steps():
    openai.api_key = ""

    with open('../../features/calculator.feature', 'r') as file:
        feature_content = file.read()

    print(feature_content)

    with open('../../py/calculator.py', 'r') as file:
        py_content = file.read()

    print(py_content)

    prompt = f"Create python code for behave step definition from ---{feature_content}--- and matching py class ---{py_content}---"

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

    with open("../../features/steps/calculator_steps.py", "w") as outfile:
        outfile.write(content)


if __name__ == '__main__':
    create_steps()