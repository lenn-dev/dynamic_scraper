'''berlinstartupjobs.com 웹사이트용 스크래퍼를 만듭니다.
스크래퍼는 다음 URL을 스크랩할 수 있어야 합니다:
https://berlinstartupjobs.com/engineering/
https://berlinstartupjobs.com/skill-areas/python/
https://berlinstartupjobs.com/skill-areas/typescript/
https://berlinstartupjobs.com/skill-areas/javascript/
첫 번째 URL에는 페이지가 있으므로 pagination 을 처리해야 합니다.
나머지 URL은 특정 스킬에 대한 것입니다. URL의 구조에 스킬 이름이 있으므로 모든 스킬을 스크래핑할 수 있는 스크래퍼를 만드세요.
회사 이름, 직무 제목, 설명 및 직무 링크를 추출하세요.'''


import requests
from bs4 import BeautifulSoup


# def scrape_data(url):
response = requests.get("https://berlinstartupjobs.com/skill-areas/javascript}/",headers={"User-Agent":"Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/121.0.0.0 Safari/537.36"})
soup = BeautifulSoup(response.content,"html.parser")
# print(soup.text)

skill_areas =[
    "python",
    "typescript",
    "javascript",  
  ]
all_jobs =[]

def scrape_data(url):
    print(f"Scrapping Berlinstartupjobs...{url}")
    response = requests.get(url,headers={"User-Agent":"Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/121.0.0.0 Safari/537.36"})
    soup = BeautifulSoup(response.content,"html.parser")
    # list
    jobs = soup.find("ul",class_="jobs-list-items").find_all("li",class_="bjs-jlid")
    # print(jobs)

    # scrape company,position,description,url
    for job in jobs:
      company = job.find("a",class_="bjs-jlid__b").text
      # print(company)
      position = job.find("h4",class_="bjs-jlid__h").text
      # print(position)
      description = job.find("div",class_="bjs-jlid__description").text
      # print(description)
      url = job.find("a")["href"]
      # print(url)

      job_data ={
        "company": company,
        "position": position,
        "description":description,
        "url": url
      }

      all_jobs.append(job_data)
    # print(len(all_jobs))
    print(all_jobs)


def scrape_skills():
    # scrape_data(f"https://berlinstartupjobs.com/skill-areas/{keyword}/")
    for x in skill_areas:
      scrape_data(f"https://berlinstartupjobs.com/skill-areas/{x}/")
      # print(len(all_jobs))

def scrape_engineer():

    def get_pages(url):
      response = requests.get(url,headers={"User-Agent":"Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/121.0.0.0 Safari/537.36"})
      soup = BeautifulSoup(response.content,"html.parser")
      pages = len(soup.find("ul",class_="bsj-nav").find_all("a"))
      return pages
      # print(pages)

    total_pages = get_pages("https://berlinstartupjobs.com/engineering/")

    for page in range(total_pages):
      scrape_data(f"https://berlinstartupjobs.com/engineering/page/{page+1}/")


scrape_skills()
scrape_engineer()
    

