import os
from openai import OpenAI

client = OpenAI(api_key=os.getenv('OPENAI_API_KEY'))

messages = [
    {"content": "Consider the terms of an arithmetic sequence: $-\\frac{1}{3}, y+2, 4y, \\ldots$. Solve for $y$.", "role": "user"},
    {"content": "For an arithmetic sequence, the difference between consecutive terms must be equal. Therefore, we can set up the following equations based on the sequence given:\n\\[ (y + 2) - \\left(-\\frac{1}{3}\\right) = 4y - (y+2) \\]\n\nSimplify and solve these equations:\n\\[ y + 2 + \\frac{1}{3} = 4y - y - 2 \\]\n\\[ y + \\frac{7}{3} = 3y - 2 \\]\n\\[ \\frac{7}{3} + 2 = 3y - y \\]\n\\[ \\frac{13}{3} = 2y \\]\n\\[ y = \\frac{13}{6} \\]\n\nThus, the value of $y$ that satisfies the given arithmetic sequence is $\\boxed{\\frac{13}{6}}$.", "role": "assistant"}
]

response = client.chat.completions.create(model="gpt-4o-mini-2024-07-18", messages=messages)

print(response.choices[0].message.content)
