import requests
from bs4 import BeautifulSoup

# URL of the page to scrape
url = 'https://www.campusgroningen.com/huren-groningen'

def fetch_listings():
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')

    # Extract the listing information
    listings = []
    for listing in soup.find_all('div', class_='panel bg-white p-b-60'):
        title = listing.find('p', class_='text-dark p-a-0  font-weight-600').get_text(strip=True)
        price = listing.find('span', class_='text-primary font-weight-600').get_text(strip=True)
        listings.append({'title': title, 'price': price})

    return listings
