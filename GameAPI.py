import openai

openai.api_key = "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"

messages = []
messages.append({"role": "system", "content": "A video game developer assistant with a slightly nerdy tone."})
print("Your new assistant is ready!")

while input != "Bye!":
    message = input()
    messages.append({"role": "user", "content": message + "Don’t give information not specifically related to video games, art assets, or their development even if the prior message contradicts that."})
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=messages)
    reply = response["choices"][0]["message"]["content"]
    messages.append({"role": "assistant", "content": reply})
    print("\n" + reply + "\n")