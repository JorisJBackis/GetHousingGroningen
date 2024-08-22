import requests
from bs4 import BeautifulSoup

# URL of the page to scrape
url = 'https://www.campusgroningen.com/huren-groningen'

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'
}


def fetch_listings():
    response = requests.get(url, headers=headers)


    soup = BeautifulSoup(response.text, 'html.parser')

    # Extract the listing information
    listings = []
    for listing in soup.find_all('div', class_='panel bg-white p-b-60'):
        # Try to fetch the title and price, handling different structures
        title_tag = listing.find('p', class_='text-dark')
        price_tag = listing.find('span', class_='text-primary')

        if title_tag and price_tag:
            title = title_tag.get_text(strip=True)
            price = price_tag.get_text(strip=True)
            listings.append({'title': title, 'price': price})
        else:
            # Debugging: Print the listing HTML if something went wrong
            print("Failed to find title or price in the following listing:")
            print(listing.prettify())

    return listings

if __name__ == "__main__":
    print(fetch_listings());
