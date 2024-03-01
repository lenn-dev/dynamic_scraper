
#Flask - 파이썬 이용해 웹사이트 구축할 수 있는 초소형 micro framework

# extractors/각각의폴더 안에 스크래핑 함수 import
# 각 파일 함수로 묶어주고 함수이름 지정해줘야 함 (함수 인자로 keyword를 보냄)
from extractors.extract_bsj import extract_bsj_jobs
from extractors.extract_wwr import extract_wwr_jobs
# file명의 file에서 function save_to_file import
from file import save_to_file

keyword = input("What do you want to search for?")

bsj = extract_bsj_jobs(keyword)
wwr = extract_wwr_jobs(keyword)

# print(f"{bsj}{wwr}")
jobs = bsj + wwr 
# TypeError: can only concatenate list (not "NoneType") to list
save_to_file(keyword,jobs)

