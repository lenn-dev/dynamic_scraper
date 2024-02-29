
from playwright.sync_api import sync_playwright
import time 
from bs4 import BeautifulSoup
import csv 

p = sync_playwright().start()
browser = p.chromium.launch(headless=False)
page = browser.new_page()

page.goto("https://www.wanted.co.kr/search?query=flutter&tab=position")


# page.goto("https://www.wanted.co.kr/")

# time.sleep(5)

# # 돋보기 버튼 클릭
# page.click("button.Aside_searchButton__Xhqq3")

# time.sleep(5)

# # 검색창 선택 후 검색어("flutter") 채워주기
# page.get_by_placeholder("검색어를 입력해 주세요.").fill("flutter")

# time.sleep(5)

# # Enter 입력
# page.keyboard.down("Enter")

# time.sleep(5)

# # 포지션탭 클릭 
# page.click("a#search_tab_position")

# time.sleep(5)

# 스크롤다운 5번
for x in range(5):
    time.sleep(5)
    page.keyboard.down("End")

#이 페이지의 html 다 스크래핑함
content = page.content()
print(content)

# p.stop()

soup = BeautifulSoup(content,"html.parser")
jobs = soup.find_all("div",class_="JobList_container__Z19Mc")

jobs_db =[]

for job in jobs:
    link = f"https://www.wanted.co.kr/{job.find('a')['href']}"
    title = job.find("strong",class_="JobCard_title__ddkwM").text
    company = job.find("span",class_="JobCard_companyName__vZMqJ").text
    reward = job.find("span",class_="JobCard_reward__sdyHn").text

    job = {
        "title": title,
        "compnay": company,
        "reward": reward,
        "link" : link,
    }
    jobs_db.append(job)

print(jobs_db)
print(len(jobs_db))

file = open("jobs.csv","w")
writer = csv.writer(file)
writer.writerow(
    [
    "Title",
    "Company",
    "Reward",
    "Link"
    ]
)

for job in jobs_db:
    writer.writerow(job.values())

file.close()



