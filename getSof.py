import requests
from bs4 import BeautifulSoup

SOF_URL = f"https://stackoverflow.com/jobs/developer-jobs-in-japan"

def get_last_page():
  result = requests.get(SOF_URL)
  soup = BeautifulSoup(result.text, "html.parser")
  pages = soup.find("div",{"class":"s-pagination"}).find_all("a")
  print(pages)
  return

def get_jobs():
  last_page = get_last_page()
  return []

