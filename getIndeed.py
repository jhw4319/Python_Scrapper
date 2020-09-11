import requests
from bs4 import BeautifulSoup

LIMIT = 50
INDEED_URL = f"https://jp.indeed.com/%E6%B1%82%E4%BA%BA?q=python&rbl=%E6%9D%B1%E4%BA%AC%E9%83%BD&jlid=b3e7700c5442df94&jt=fulltime&limit={LIMIT}"


def get_last_pages():
    result = requests.get(INDEED_URL)
    soup = BeautifulSoup(result.text, "html.parser")

    div_pagination = soup.find("div", {"class": "pagination"})

    page_link = div_pagination.find_all('a')
    pages = []

    for link in page_link[:-1]:
        pages.append(int(link.string))

    max_page = pages[-1]
    return max_page


def extract_job(html):
    title = html.find("h2", {"class": "title"}).find("a")["title"]
    company = html.find("span", {"class": "company"})
    company_anchor = company.find("a")
    if company_anchor is not None:
        company = str(company_anchor.string)
    else:
        company = str(company.string)
    company = company.strip()
    location = html.find("div", {"class": "recJobLoc"})["data-rc-loc"]
    job_id = html["data-jk"]
    return {
        "title": title,
        "company": company,
        "location": location,
        "link": f"https://jp.indeed.com/viewjob?jk={job_id}"
    }


def extract_jobs(last_page):
    jobs = []
    for page in range(last_page):
        result = requests.get(f"{INDEED_URL}&start={page*LIMIT}")
        soup = BeautifulSoup(result.text, "html.parser")
        results = soup.find_all("div", {"class": "jobsearch-SerpJobCard"})
        for result in results:
            job = extract_job(result)
            jobs.append(job)
        return jobs

def get_jobs():
  last_page = get_last_pages()
  jobs = extract_jobs(last_page)
  return jobs