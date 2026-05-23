import tkinter as tk
from rules import rules_list
from google import genai # pip install google-genai

client = genai.Client()

def onclick():
    user_prompt = prompt_entry.get()

    prompt = (f"Виконай запит користувача: {user_prompt}\n"
              "Обов'язково виконуй наступні правила:\n"
              f"{'\n'.join(rules_list)}")

    response = client.models.generate_content(
        model="gemini-2.5-flash",
        contents=prompt,
    )

    response_label.config(text=str(response.text))

window = tk.Tk()
window.title("Візуальний асистент")
window.geometry("300x400")

response_label = tk.Label(text="Response")
response_label.pack()


prompt_btn = tk.Button(text="Відправити", command=onclick)
prompt_btn.pack(side="bottom", fill="x")

prompt_entry = tk.Entry()
prompt_entry.pack(side="bottom", fill="x")

window.mainloop()