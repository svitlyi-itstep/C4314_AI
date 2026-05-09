import os
import json

if os.path.exists("user.json"):
    with open("user.json", "r", encoding="utf-8") as file:
        user = json.load(file)

    print("Привіт,",user.get("name"), "!")
    print("Тобі ",user.get("age"), "років.")
else:
    name = input("Як тебе звуть? ")
    age = input("Скільки тобі років? ")

    with open("user.json", "w", encoding="utf-8") as file:
        json.dump({
            "name": name,
            "age": age
        }, file)

