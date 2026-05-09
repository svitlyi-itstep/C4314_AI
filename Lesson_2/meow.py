import requests

params = {
    "count": input("Скільки фактів бажаєте отримати? "),
    "lang": input("Якою мовою хочете отримати факти? ")
}

url = f"https://meowfacts.herokuapp.com/"
response = requests.get(url, params)

if response.ok:
    facts = response.json().get("data")
    print("Випадкові факти про котів:")
    for fact in facts:
        print("—", fact)
else:
    response.raise_for_status()

'''

    Зробити так, щоб програма запам'ятовувала останні
    конфігурації користувача для meowfacts (кількість
    фактів та мову).
    
    Конфігурації мають зберігатися у файлі у форматі JSON.
    
'''