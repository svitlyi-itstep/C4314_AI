import tkinter as tk
from tkinter import scrolledtext
from rules import rules_list
from google import genai # pip install google-genai

client = genai.Client()

def print_message(message, tag="response"):
    chat_scrolled.configure(state="normal")
    chat_scrolled.insert("end", message + "\n\n", tag)
    chat_scrolled.configure(state="disabled")
    chat_scrolled.see("end")

def onclick(event=None):
    user_prompt = prompt_entry.get()

    if not user_prompt: return
    try:
        prompt_entry.delete(0, "end")
        print_message(user_prompt, tag="prompt")

        prompt = (f"Виконай запит користувача: {user_prompt}\n"
                  "Обов'язково виконуй наступні правила:\n"
                  f"{'\n'.join(rules_list)}")

        response = client.models.generate_content(
            model="gemini-2.5-flash",
            contents=prompt,
        )
        # response_label.config(text=str(response.text))
        print_message(str(response.text), "response")
    except Exception as e:
        print(e)

window = tk.Tk()
window.title("Візуальний асистент")
window.geometry("300x400")

response_label = tk.Label(text="Response")
response_label.pack()

chat_scrolled = scrolledtext.ScrolledText(height=20, state="disabled",
                wrap="word")
chat_scrolled.pack(fill="both", expand=True)

chat_scrolled.tag_config("response", foreground="gray", justify="left")
chat_scrolled.tag_config("prompt", foreground="green", justify="right")


prompt_btn = tk.Button(text="Відправити", command=onclick)
prompt_btn.pack(side="bottom", fill="x")

prompt_entry = tk.Entry()
prompt_entry.pack(side="bottom", fill="x")
prompt_entry.bind("<Return>", onclick)

window.mainloop()