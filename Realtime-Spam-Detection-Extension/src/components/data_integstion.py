import requests
from bs4 import BeautifulSoup
import re
from src.exception.custom_exception import ProjectException
import sys
from src.trained_model.model import Model
import warnings

warnings.filterwarnings('ignore')
class ScrapedData:

    def __init__(self, url=0):
        self.url = url
        self.model = Model()
        self.model.load_model()

    # Scrape visible text from a URL
    def scrape_text_from_url(self,url: str) -> str:
        try:
            response = requests.get(url, timeout=10)
            soup = BeautifulSoup(response.text, 'html.parser')

            # Remove script and style elements
            for tag in soup(['script', 'style', 'header', 'footer', 'nav']):
                tag.decompose()

            text = soup.get_text(separator=' ', strip=True)

            # Clean multiple spaces and special characters
            text = re.sub(r'\s+', ' ', text)
            text_list = text.split(".")
            print(text_list)
            return text_list

        except Exception as e:
            print(f"[Error] Failed to scrape the URL: {e}")
            ProjectException(e,sys)
            return ""

    # Main logic to check spam from URL
    def check_url_for_spam(self,url: str):
        try:
            print(f"Checking URL: {url}")
            scraped_list =self.scrape_text_from_url(url)
            result_dict={}
            print("Total len ",len(scraped_list))
            if len(scraped_list) > 170:
                scraped_list = scraped_list[:170]
            print(len(scraped_list))
            if scraped_list:
                for scraped_text in scraped_list:
                    
                    scraped_text = scraped_text.strip()
                    if not scraped_text:
                        continue
                        
                    if len(scraped_text) > 512:
                        scraped_text = scraped_text[:512]
                    
                    result = self.model.predict(scraped_text)  # limit to 512 tokens
                    print(result)
                    if result in result_dict:
                        result_dict[result] += 1
                    else:
                        result_dict[result] = 1
            
            else:
                print("Failed to extract content from the link.")
                return None
            return max(result_dict, key=result_dict.get)
        
        except Exception as e:
            ProjectException(e,sys)
            print("Error ",e)
            return None
