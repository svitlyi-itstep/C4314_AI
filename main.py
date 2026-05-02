from google import genai # pip install google-genai
from rules import rules_list


client = genai.Client(api_key="AIzaSyAeOJBxdhbhEVgkDPe0V_kv2XdmY6jZm6o")

print(" - Асистента запущено! -")

while True:
    user_prompt = input("\n> ")

    if user_prompt in ["exit", "quit", "stop"]:
        break

    prompt = (f"Виконай запит користувача: {user_prompt}\n"
              "Обов'язково виконуй наступні правила:\n"
              "\n".join(rules_list))

    # Доступні моделі:
    # gemini-3-flash-preview
    # gemini-2.5-flash

    response = client.models.generate_content(
        model="gemini-3-flash-preview",
        contents=prompt,
    )

    print("\n", response.text)
