import os

from groq import Groq

client = Groq(
    api_key="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"
)

while True:
    prompt = str(input("Starting: ")),
    prompt = (prompt, ", Now write a complete story using this as a starting. Minimum of 500 lines and a with a suitable title"),
    prompt = str(prompt)
    chat_completion = client.chat.completions.create(
        messages=[
            {
                "role": "user",
                "content": prompt,
            }
        ],
        model="llama3-8b-8192",
    )
    a = chat_completion.choices[0].message.content
    print(a)
