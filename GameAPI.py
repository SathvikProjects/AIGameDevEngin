import openai

openai.api_key = "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"
#This key is for example purposes only

messages = []
sysin = input("What type of chatbot would you like to create?\n")
messages.append({"role": "system", "content": sysin})

print("Your new assistant is ready!")
while input != "See ya later!":
    message = input()
    messages.append({"role": "user", "content": message})
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=messages)
    reply = response["choices"][0]["message"]["content"]
    messages.append({"role": "assistant", "content": reply})
    print("\n" + reply + "\n")