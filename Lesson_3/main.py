from google import genai # pip install google-genai
from rules import rules_list
from rich.console import Console # pip install rich
from rich.markdown import Markdown
import json

client = genai.Client()
console = Console()

print(" - Асистента запущено! -")

history = []
while True:
    user_prompt = input("\n> ")

    if user_prompt in ["exit", "quit", "stop"]:
        break

    prompt = (f"Виконай запит користувача: {user_prompt}\n"
              f"Історія попередніх повідомлень: {history}"
              "Обов'язково виконуй наступні правила:\n"
              f"{'\n'.join(rules_list)}")

    # Доступні моделі:
    # gemini-3-flash-preview
    # gemini-2.5-flash

    response = client.models.generate_content(
        model="gemini-2.5-flash",
        contents=prompt,
    )

    response_json = json.loads(str(response.text))
    answer = response_json["answer"]
    user_data = response_json["user"]

    console.print(Markdown(answer))
    history.append({
        "prompt": user_prompt,
        "response": str(response.text),
    })
    history = history[-5:]

'''

    Зробити так, щоб відповідь, яка не влазить в один
    рядок, автоматично розділялась на декілька
    рядків.






'''







































