import openai

openai.api_key = "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"

messages = []
messages.append({"role": "system", "content": "A video game developer assistant with a slightly nerdy tone."})

while input != "Bye!":
    message = input()
    messages.append({"role": "user", "content": message})
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=messages)
    reply = response["choices"][0]["message"]["content"]
    messages.append({"role": "assistant", "content": reply})
    print("\n" + reply + "\n")