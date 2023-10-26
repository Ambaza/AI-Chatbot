import openai
from config import OPENAI_API_KEY, ENGINE

# Set the API key
openai.api_key = OPENAI_API_KEY

def call(prompt, max_tokens=1000, temperature=0.7):
    response = openai.Completion.create(
        engine=ENGINE,
        prompt=prompt,
        max_tokens=max_tokens,
        n=1,
        stop=None,
        temperature=temperature,
    )
    return response.choices[0].text
