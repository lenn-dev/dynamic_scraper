
import requests
from bs4 import BeautifulSoup

def extract_bsj_jobs(keyword):

  # def scrape_data(url):
  response = requests.get("https://berlinstartupjobs.com/skill-areas/javascript}/",headers={"User-Agent":"Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/121.0.0.0 Safari/537.36"})
  soup = BeautifulSoup(response.content,"html.parser")
  # print(soup.text)

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
        # description = job.find("div",class_="bjs-jlid__description").text
        # print(description)
        url = job.find("a")["href"]
        # print(url)

        job_data ={
          "position": position,
          "company": company,
          # "description":description,
          "link": url
        }

        all_jobs.append(job_data)
      # print(len(all_jobs))
      print(all_jobs)


  def scrape_skills(keyword):
      scrape_data(f"https://berlinstartupjobs.com/skill-areas/{keyword}/")
     
  scrape_skills(keyword)
  return all_jobs

# extract_bsj_jobs("javascript")  

