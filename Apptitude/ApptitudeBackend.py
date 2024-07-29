from ai21 import AI21Client
from config import *

client = AI21Client(api_key=config["Ai21-Apikey"])


def answer_genai(prompt):
    # Call AI21 API to summarize text
    response = client.completion.create(
        model="j2-ultra",
        prompt=prompt,
        num_results=1,
        max_tokens=8000,
        temperature=0.1,
    )

    # st = response['completions'][0]['data']['text']
    # st = response['completions'][0]['data']['text']
    return response.completions[0].data.text
    # print(response.completions[0].data.text)
    # return st


# print(config["Ai21-Apikey"])
result = """"""
result = answer_genai(
    """Generate 10 multiple-choice questions on the topic of quantitative aptitude. \
    Each question should include four answer options \
    (A, B, C, D) and the correct answer should be listed at the end.\
    The questions should cover a variety of concepts such as \
    arithmetic, algebra, geometry, and data interpretation. Ensure that\
    the questions are clear and the options are well-distributed to avoid giving away the correct answer easily."""
)
print(result)
