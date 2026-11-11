import json
from groq import Groq
from dotenv import load_dotenv
import os

load_dotenv()

client = Groq()
system_prompt = ""
with open("system_prompt.txt", "r") as file:
    system_prompt = file.read()

message = [
    { "role": "system", "content": system_prompt },
]
def run_command(command):
    result = os.system(command)
    return result


available_tools = {
      "run_command":{
            "fn": run_command,
            "desciption":"Takes command as input and runs it"
      }
}
while True:
    query = input("> ")
    message.append({ "role": "user", "content": query })
    while True:
        chat_completion = client.chat.completions.create(
            response_format={"type":"json_object"},
            messages=message,
            model="openai/gpt-oss-120b",
        )
        parsed_res = json.loads(chat_completion.choices[0].message.content)
        message.append({"role":"assistant","content":json.dumps(parsed_res)})

        if parsed_res.get('step') == "plan":
                print(f"🧠: {parsed_res.get('content')}")
                continue

        if parsed_res.get('step') == "action":
                tool_name = parsed_res.get("function")
                tool_input = parsed_res.get("input")
                if tool_name in available_tools:
                        output = available_tools[tool_name].get("fn")(tool_input)
                        message.append({
                            "role": "user",
                            "content": json.dumps({
                                "step": "verification",
                                "output": output
                            })
                        })
                continue

        if parsed_res.get('step') == "output":
            print(f"🧠: {parsed_res.get('content')}")
            break