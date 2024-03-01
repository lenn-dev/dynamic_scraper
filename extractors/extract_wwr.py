import requests
from bs4 import BeautifulSoup

def extract_wwr_jobs(keyword):
    
  all_jobs = []

  def scrape_data(url):
      print(f"Scrapping Weworkremotely...{url}") #디버깅을 위한 출력
      response = requests.get(url)
      # print(response.content)
      soup = BeautifulSoup(
          response.content,
          "html.parser",
      )
      jobs = soup.find("section", class_="jobs").find_all("li")[1:-1]
      # print(jobs)
      for job in jobs:
        # title = job.find("span", class_="title").text
        company, position, location = job.find_all("span", class_="company")
        # url = job.find("div",class_="tooltip").next_sibling["href"]
        link = job.find("a")["href"]
        # if url:
        #    url = url["href"]
        job_data = {
          # "title": title,
          "position": position.text,
          "company": company.text,
          # "location": location.text,
          "link": f"https://weworkremotely.com{url}",
        }
        all_jobs.append(job_data)


    # 스크래핑할 페이지가 몇개인지 알아내는 함수
    # 페이지 버튼을 찾아서 몇개인지 확인 후 페이지 수만큼 scrape_data 함수를 불러서 다른 주소값을 주면서 스크랩핑 할 예정
  def get_pages(url):
      response = requests.get(url)
      soup = BeautifulSoup(response.content,"html.parser")
      buttons= len(soup.find("div",class_="pagination").find_all("span",class_="page"))
      return buttons
    # print(buttons)

  total_pages = get_pages("https://weworkremotely.com/remote-full-time-jobs?page=1")
  for x in range(total_pages):
      url = f"https://weworkremotely.com/remote-full-time-jobs?page={x+1}"
      # print(url)
      scrape_data(url)
      # print(len(all_jobs))
      # print(all_jobs)

  return(all_jobs)
  # print(all_jobs)
  # print(list(filter(lambda item : item['title'] == keyword, all_jobs)))

  # keyword_search = [ item for item in all_jobs if item["title"] == keyword ]
  # print(keyword_search)
  # return keyword_search


# usage
# extract_wwr_jobs("Contact Researcher")