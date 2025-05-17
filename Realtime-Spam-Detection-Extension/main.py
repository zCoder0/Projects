from src.components.data_integstion import ScrapedData
from src.exception.custom_exception import ProjectException
import sys
try:
    #url = input("Enter url ")
    url="https://www.geeksforgeeks.org/introduction-to-java/"
    data=ScrapedData()
    result = data.check_url_for_spam(url)
    print(result)
except Exception as e:
    print(f"An error occurred: {e}")
    ProjectException(e,sys)