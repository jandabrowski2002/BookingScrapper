from urllib import response
import requests

url = "https://www.booking.com/hotel/pl/happy-tower.pl.html"
response = requests.get(url)
print(response.status_code)
print(response.text)