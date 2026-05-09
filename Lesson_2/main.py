import requests # pip install requests

url = "https://www.whenisthenextmcufilm.com/api"

response = requests.get(url)

if response.ok:
    film = response.json()
    print()
    print(f'{film.get("title")} releases in {film.get("days_until")} day(s)')
    print('Release Date:', film.get("release_date"))
    print('Production Type:', film.get("type"))
    print(film.get("overview"))
    print('What`s afterwards?', film.get("following_production").get("title"))
else:
    response.raise_for_status()