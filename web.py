import requests
from bs4 import BeautifulSoup

url = 'https://usu.edu.au/events/'
response = requests.get(url)
response.raise_for_status() 
soup = BeautifulSoup(response.text, 'html.parser')

# Find all <div> elements with class 'event'
events = soup.find_all('div', class_='EventCard-module--EventCard--3dc8c')

# Print the complete HTML of each event
for card in events:
    # Find the <a> tag within the current event card
    link = card.find('a', class_='EventCard-module--link--6562a')
    
    if link:
        # Extract the href attribute
        href = link.get('href')
        print(f"Event URL: {href}")

    print("-" * 40)