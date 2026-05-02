from google import genai # pip install google-genai

client = genai.Client(api_key="AIzaSyC_laWNtFHjahkANIMfgzSBuz4M0d06dVw")

print(" - Асистента запущено! -")
user_prompt = input("\n> ")

response = client.models.generate_content(
    model="gemini-3-flash-preview",
    contents=user_prompt,
)

print("\n", response.text)


'''
    Зробити так, щоб при запуску програми користувач міг ввести власний
    запит до штучного інтелекту. Програма має вивести відповідь на запит
    користувача.
    
    Використати команду input() та змінні.
    
    Зробити так, щоб можна було вводити декілька запитів, не перезапускаючи код.
'''