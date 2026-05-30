import tkinter as tk
from tkinter import scrolledtext
from rules import rules_list
from google import genai # pip install google-genai
from PIL import Image, ImageTk # pip install pillow
import json

client = genai.Client() # api_key="<KEY>"
emotions = {}

def print_message(message, tag="response"):
    chat_scrolled.configure(state="normal")
    chat_scrolled.insert("end", message + "\n\n", tag)
    chat_scrolled.configure(state="disabled")
    chat_scrolled.see("end")

def load_emotions():
    global emotions
    # Normal emotion
    img = Image.open("img/normal.png").resize((100, 80))
    emotions["normal"] = ImageTk.PhotoImage(img)

    # Thinking emotion
    img = Image.open("img/thinking.png").resize((100, 100))
    emotions["thinking"] = ImageTk.PhotoImage(img)

def change_emotion(emotion):
    emotion_label.config(image=emotions[emotion])

def onclick(event=None):
    user_prompt = prompt_entry.get()

    if not user_prompt: return
    try:
        prompt_entry.delete(0, "end")
        print_message(user_prompt, tag="prompt")

        prompt = (f"Виконай запит користувача: {user_prompt}\n"
                  "Обов'язково виконуй наступні правила:\n"
                  f"{'\n'.join(rules_list)}\n"
                  f"Доступні емоції: {emotions.keys()}")

        response = client.models.generate_content(
            model="gemini-2.5-flash",
            contents=prompt,
        )
        response_json = json.loads(str(response.text) \
                         .removeprefix("```json") \
                         .removesuffix("```"))
        answer, emotion = response_json["answer"], response_json["emotion"]
        # response_label.config(text=str(response.text))
        print_message(answer, "response")
        change_emotion(emotion)
    except Exception as e:
        print(e)

window = tk.Tk()
window.title("Візуальний асистент")
window.geometry("300x400")

load_emotions()
emotion_label = tk.Label()
emotion_label.pack()
change_emotion("normal")

chat_scrolled = scrolledtext.ScrolledText(height=15, state="disabled",
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