import requests

url = "YOU MUST INPUT BASE URL OF YOUR API"
access_key = "YOU MUST INPUT YOUR API KEY."

sehir = input("şehir: ")

response = requests.get(url, params= {
    "key": access_key,
    "q": sehir,
    "lang": "ing"
})

sonuc = response.json()

sehir = sonuc["location"]["name"]
havadurumu = sonuc["current"]["temp_c"]
text = sonuc["current"]["condition"]["text"]

print(f"{sehir} is {havadurumu} degree and  {text.lower()} at the moment.")
