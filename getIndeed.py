import requests
from bs4 import BeautifulSoup

INDEED_URL = "https://jp.indeed.com/%E6%B1%82%E4%BA%BA?q=python&rbl=%E6%9D%B1%E4%BA%AC%E9%83%BD&jlid=b3e7700c5442df94&jt=fulltime&limit=50"

def extract_indeed_pages():
  result = requests.get(INDEED_URL)
  soup = BeautifulSoup(result.text, "html.parser")

  div_pagination = soup.find("div", {"class":"pagination"})

  page_link = div_pagination.find_all('a')
  pages = []

  for link in page_link[:-1]:
    pages.append(int(link.string))

  max_page = pages[-1]
  return max_page

def extract_indeed_jobs(last_page):
  jobs = []
  for page in range(last_page):
    result = requests.get(INDEED_URL)
    soup = BeautifulSoup(result.text, "html.parser")
    results = soup.find_all("div", {"class":"jobsearch-SerpJobCard"})
    return jobs