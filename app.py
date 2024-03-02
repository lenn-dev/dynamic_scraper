# 혹시 vscode로 하시는 분들 중 코드 수정된거 터미널 실행 멈추고 다시 실행하는 번거로움이 싫으신분 자동 리로드 실행 코드입니다.
# export FLASK_APP = main.py
# export FLASK_ENV = development
# flask run

from flask import Flask, render_template, request
from extractors.extract_bsj import extract_bsj_jobs
from extractors.extract_wwr import extract_wwr_jobs

app = Flask("JobScrapper")

# fake db : 서버가 켜져있을 때에만 메모리에 있음
# extract한 data를 db에 저장해두고,검색이 반복될때 꺼내서 출력하기
# 같은 검색어에 대해 web페이지 스크래핑을 반복할 필요 없으니 동작시간 축소 가능
db = {}

# 함수를 만들어 인자에 들어간 주소로 보내주고 바로 밑의 함수 호출 해줌
# 함수가 html 코드를 반환할 수 있는데, 더 많은 html 코드를 보내고 싶다면
# templates 폴더를 만들어 별도 파일 생성 
# 다른이름의 폴더는 안된다. Flask는 templates 란 이름의 폴더를 찾기 때문
# main.py 파일과 같은 레벨에 있어야지 상/하 레벨에 있으면 안됨
@app.route('/')
def home():
#    render_template() 함수는 Flask가 templates 폴더를 찾아보고 원하는 파일을 찾게 함
#    html코드를 templates 폴더에 따로 작성해서 그 파일을 렌더해달라는 함수를 return
#    함수 인자로 변수도 함께 보낼 수 있음
   return render_template("home.html",name="lenn")
#    return "<h1>This is Home!<h1><a href='/hello'>go to hello</a>"

@app.route('/search')
def search():
#    requesr의 arguments에서 keyword를 가져올 수 있음
#    가져온 keyword를 template를 보내 user가 뭘 search하는지 알수 있음
    keyword =request.args.get("keyword")
    if keyword in db:
        jobs = db[keyword]
    else:
        bsj = extract_bsj_jobs(keyword)
        wwr = extract_wwr_jobs(keyword)
        jobs = bsj + wwr
        db[keyword] = jobs 
    
    return render_template("search.html",keyword=keyword,jobs=jobs)




app.run("0.0.0.0")
# app.run("127.0.0.1", port=8000, debug=True)
# if __name__ == '__main__':  
#    app.run('0.0.0.0',port=5000,debug=True)

# user가 어떤 job 을 찾고 있는지 입력할 수 있는 form 만들기


