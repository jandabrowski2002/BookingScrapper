from bs4 import BeautifulSoup
import requests

url = "https://www.booking.com/hotel/pl/happy-tower.pl.html#tab-reviews"
response = requests.get(url)

page_dom  = BeautifulSoup(response.text, 'html.parser')

reviews = page_dom.select("review_list_new_item_block")
print(len(reviews))

