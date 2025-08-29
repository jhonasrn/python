# news_scraper.py
import requests
from bs4 import BeautifulSoup

class NewsScraper:
    def __init__(self, url="https://news.google.com"):
        self.url = url
    
    def scrape_headlines(self, limit=10):
        try:
            response = requests.get(self.url)
            response.raise_for_status()
            
            soup = BeautifulSoup(response.text, 'html.parser')
            headlines = soup.find_all('h3')[:limit]
            
            print("📰 Latest News Headlines:")
            for i, headline in enumerate(headlines, 1):
                print(f"{i}. {headline.get_text()}")
                
        except requests.RequestException as e:
            print(f"Error accessing website: {e}")
        except Exception as e:
            print(f"An error occurred: {e}")

if __name__ == "__main__":
    scraper = NewsScraper()
    scraper.scrape_headlines()