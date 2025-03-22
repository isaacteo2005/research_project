from openai import OpenAI
import time
secret_key = "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"
client = OpenAI(
    api_key = secret_key
)
def use_prompt(text_prompt, repeat):
    chat_log = []
    times = repeat
    with open("events.txt", "r") as infile:
        while True:
            #reads each name in the file
            line = infile.readline()
            if not line:
                 break
            #repeats a number of times based off parameter
            while times > 0:
                 #gets a new response each time repeated
                 next_message = text_prompt + line.strip()
                 chat_log.append({"role": "user", "content": next_message})
                 response = client.chat.completions.create(
                model = "gpt-3.5-turbo",
                messages = chat_log
                )
                 assistant_response = response.choices[0].message.content
                 print("ChatGPT:", assistant_response.strip("\n").strip())
                 print(".................\n")
                 chat_log.append({"role": "assistant", "content": assistant_response.strip("\n").strip()})
                 times = times - 1
            times = repeat

use_prompt("Tell me about this event: ", 2)