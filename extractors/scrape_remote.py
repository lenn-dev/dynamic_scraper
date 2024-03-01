import requests 
from bs4 import BeautifulSoup
# keywords 목록에 들어있는 Keyword 에 해당하는 일자리를 검색하여 스크래핑하기
keywords = [
  "flutter",
  "python",
  "golang"
]
# "table", id_="jobsboard"
# "tr","data-search"

# 사이트 검색창에 키워드 넣으면 주소창에 아래와 같은 형식의 주소생성됨
# https://remoteok.com/remote-flutter-jobs

response = requests.get("https://remoteok.com/remote-flutter-jobs",headers={"User-Agent":"Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/121.0.0.0 Safari/537.36"})

# status_code 출력해보면 차단당한걸 알 수 있음 
# 503 에러 - 굉장히 일반적인 차단- 우회해야 함
'''네트워크 페널에 가서 status 가 200이고 type이 document인 request 보면 remote-flutter-jobs라고 나옴. 그 request 클릭하면 오른쪽에 정보들이 나옴. 스크롤 다운해서 request headers (우리 브라우저가 서버에 보내는 정보: 어떤 쿠키가 있는지 encoding 정보는 accept 하는지, http를 원하는지..등등의 정보가 있음)를 찾기. 여기에 user agent 찾기(클라이언트가 누구인지에 대한 정보)
이 user agent 부분을 복사해두고 우리가 remoteok로 requests를 생성할때 header를 함께 전달
우리는 remoteok를 속여서 웹사이트에서 접근한다고 생각하게 만들것임'''
# print(response.content)
print(response.status_code)
# b'<html>\n<head><title>503 Service Temporarily Unavailable</title></head>\n<body>\n<center><h1>503 Service Temporarily Unavailable</h1></center>\n<hr><center>nginx</center>\n</body>\n</html>\n'
# 503




# soup = BeautifulSoup(response.content,"html.parser")
# print(soup.find("table",id_="jobsboard"))

