# print("Hello World")
# 파이썬 실행시켜주는 방법
# 터미널에 python main.py를 적어주면 됨

from playwright.sync_api import sync_playwright
import time #대기시간 생성해서 실행속도 늦춰서 작업을 확인하기 위해 쓸예정
from bs4 import BeautifulSoup
import csv # csv파일 작성

#  sync_playwright() 함수 cmd+클릭해보면 단순히 class를 instanciate해주는 함수인걸 알 수 있음
p = sync_playwright().start()

# p. 쓰면 사용할 브라우저 종류들 뜸. chrom 선택
# lauch() 로 브라우저 초기화
browser = p.chromium.launch(headless=False)

# 새로운 페이지 제공
page = browser.new_page()

# 여기에 스크래핑 하고 싶은 웹의 탭주소를 클릭해서 들어가 주소를 그대로 넣어도 되지만 
# playwright 활용하면 나 대신 웹사이트에 방문해 클릭하고 검색해줄 수 있다.
page.goto("https://www.wanted.co.kr/search?query=flutter&tab=position")

# # 웹사이트 메인페이지 => 돋보기클릭 => 검색창클릭 => 검색어입력 => enter => 5초기다리기 => position 탭 클릭 => 스크롤다운 3번 => html 가져오기
# page.goto("https://www.wanted.co.kr/")

# # #5초동안 멈춤
# time.sleep(5)

# # 페이지에서 돋보기 버튼 클릭
# # click("selector.className")
# page.click("button.Aside_searchButton__Xhqq3")


# time.sleep(5)

# # 다음페이지에서 검색창 선택
# # input의 class 이름으로 찾아도 되지만 class name은 언제든 변경 가능하니
# # placeholder 가 있다면 직접 선택해도 됨(이건 변하지 않을테니까?)
# # text area로 바꾸든 class name을 바꾸든 해도 이 placeholder를 찾을 수 있을 것임
# # 검색창에 검색어("flutter") 채워주기
# page.get_by_placeholder("검색어를 입력해 주세요.").fill("flutter")

# time.sleep(5)

# # enter 치기
# page.keyboard.down("Enter")

# time.sleep(5)

# # 포지션 클릭 click("selector#id name")
# page.click("a#search_tab_position")

# time.sleep(5)

# 스크롤다운 : 키보드의 End키를 눌러야 함(페이지 맨 밑으로 가는 버튼)
# 실제 키보드에 없어도 명령어는 알아들음
# mac에서는 cmd + 위/아래 방향키

for x in range(5):
    time.sleep(5)
    page.keyboard.down("End")

#이 페이지의 html 다 스크래핑함

content = page.content()
# print(content)


# p.stop()
# playwright을 initialise 해야 하니까 브라우저를 열면 play를 멈춰야함
# 그래야 메모리 누수가 없음

soup = BeautifulSoup(content,"html.parser")

#job list 반환
jobs = soup.find_all("div",class_="JobList_container__Z19Mc")

#  모든 일자리 포함하는 div 태그인지 확인하려고 
# print(jobs)

# job dictionary 저장할 배열
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


# exporting to exel
# csv : comma seperated values
# csv open viewer / excel viewer 익스텐션은 csv파일을 엑셀형식으로 보여줌
    
# open() 내장함수 사용해 파일을 열어주거나 없다면 만들어준다
# 내장함수 살펴보면 디폴트로 "r" 모드(읽기모드) 로 되어 있는데,
# 수정가능한 모드 "w"로 바꿔준다.
file = open("jobs.csv","w")
#  csv 파일에 행을 추가할 수 있는 csv모듈과 writer함수 사용함
writer = csv.writer(file)

#  writerow() 메서드는 인자로 리스트를 받는데 jobs_db 안의 job이 dictionary 형식이라 수정해야함
#  values() 내장함수를 이용하면 dictionary에서 value 값만 추출해 리스트로 반환함
#  반대로 key 값만 추출하고 싶다면 keys() 사용하면 됨
#  여기서 추출하는 목록의 이름만 적어주는 것은 csv 형식이 exel 형식으로 바뀌려면
#  "Title","Company","Reward","Link"
#  dev_ops, nomad, 10000, http://
#  이런식으로 행(row)마다 적어줘야 엑셀 표 형식으로 나오기 때문
#  csv 파일을 만들어서 위처럼 작성한 후 csv open viewer 로 보면 확인가능함
#  writerow() 메서드는 가져온 value를 콤마로 구분하고 자동줄바꿈까지 해줌

#  header 줄 작성
writer.writerow(
    [
    "Title",
    "Company",
    "Reward",
    "Link"
    ]
)
# 추출 목록 아랫줄에 쓰여질 value들을 jobs_db 돌면서
# job dictionary 안의 value 값만 추출해
# 미리 생성해둔 쓰기모드인 csv 파일 writer에 writerow() 메서들을 이용해 쓰기.
# 이렇게 하면 스크래핑 한 정보들을 csv파일로 저장할 수 있음.
for job in jobs_db:
    writer.writerow(job.values())

file.close()



#여기서 실행시키면 브라우저가 안나타남
# screenshot 찍어서 확인해볼 것임. 
# 스크린샷 저장할 파일확장자와 파일 이름을 path에 적고 실행하면
# 파일 아래 생성되어 있음
# page.screenshot(path="screenshot.png")

#브라우저는 실행되고 있지만 볼 수는 없음
# 이는 headless mode라는 것 때문
# 내 컴퓨터에서 실행하고 있지만 
# playwright의 default설정이 브라우저를 보여주지 않고 실행시키는 것임
# lauch() 함수 안의 인자로 headless=False로 설정해주면
# 브라우저 떴다가 스크린샷 찍고 자동으로 종료함


