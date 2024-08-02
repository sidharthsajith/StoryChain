from groq import Groq

client = Groq(
    api_key="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"
)

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
story = chat_completion.choices[0].message.content
print(story)

while True:
    revamp = str(input("Do you want to add anything to the story? \n 1) New Characters \n 2) New Plot \n 3) A Twist \n 4) No its fine (quit) \n \t Please Elaborate what all revamps would you like to make to the story: "))
    if revamp.lower == quit:
        print("GoodBye")
        break
    prompt = (story,"   This is the story so far, Now I want you to make some revamps like: ",revamp, "And give me the newly revamped story.")
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
    story = chat_completion.choices[0].message.content
    print(story)
