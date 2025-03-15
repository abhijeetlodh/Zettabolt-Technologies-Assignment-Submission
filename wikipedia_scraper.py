import requests
from bs4 import BeautifulSoup
import re

class WikipediaScraper:
    def __fetch_page(self, url):
        try:
            response = requests.get(url)
            if response.status_code == 200:
                return response.text
            else:
                raise Exception(f"Failed to fetch page: {url}")
        except requests.RequestException as e:
            print(f"Error fetching page: {e}")
            return None

    def parse_content(self, html):
        if html is None:
            return None
        soup = BeautifulSoup(html, 'html.parser')
        content_div = soup.find(id='mw-content-text')
        if content_div:
            return str(content_div)
        else:
            print("Main content not found")
            return None

    def clean_text(self, text):
        if text is None:
            return ""
        clean_text = re.sub(r'<.*?>', '', text)  # Remove HTML tags
        clean_text = re.sub(r'\[\d+\]', '', clean_text)  # Remove references like [1]
        return clean_text

    def split_into_chunks(self, text):
        if not text:
            return []
        chunks = text.split('\n\n')
        return [chunk.strip() for chunk in chunks if chunk.strip()]

    def get_chunks(self, url):
        html = self.__fetch_page(url)
        content = self.parse_content(html)
        clean_text = self.clean_text(content)
        chunks = self.split_into_chunks(clean_text)
        return chunks

if __name__ == "__main__":
    # Test the class
    scraper = WikipediaScraper()
    url = "https://en.wikipedia.org/wiki/Artificial_intelligence"
    chunks = scraper.get_chunks(url)
    print(f"Extracted {len(chunks)} chunks")