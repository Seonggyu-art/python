# import calendar

# calendar.prcal(2024)  # 달력 뽑아줌

# calendar.prmonth(2024, 12)  # 24녀 12월 달력만 뽑아줌

# print(calendar.weekday(2024, 12, 11)) #0부터 11번째? 날짜 알려줌
# print(calendar.weekday(2024, 12, 15))
# //////////////////////////////////////////////

# import datetime

# days = ['월', '화', '수', '목', '금', '토', '일']
# weekday = datetime.date.today().weekday()
# print('오늘은 ' +days[weekday]+ '요일')

# weekday = datetime.date(2025, 12, 25).weekday()
# print('크리스마스는 ' + days[weekday]+'요일')

# ///////////////////////////////////////////////

# import datetime

# def get_weekday(yyyy, mm, dd):
#     days = ['월', '화', '수', '목', '금', '토', '일']
#     idx = datetime.date(yyyy, mm, dd).weekday()
#     print("{}년 {}월 {}일 {}요일".format(yyyy, mm, dd, days[idx]))

# # 함수 호출 예시
# get_weekday(2024, 8, 15)

# ///////////////////////////////////////

# import time
# a = time.time()
# time.sleep(2)
# b = time.time()
# print(b-a)

# # /////////////////////////////

# # import time
# print(time.localtime())
# time_str = time.localtime()
# print(time_str.tm_year)

# print(time.ctime())
# print(time.ctime(a))
# print(time.ctime(b))
# //////////////////////////////////////

#  1970년 1월 1일 기준
# year = round(time.time()/(365*24*60*60))
# print(year)
# day = time.time()/(24*60*60)
# print(day)

# start = time.time()

# for i in range(10):
#     print(i)
#     time.sleep(1)

# end = time.time()
# print(f"수행 시간 : {end-start}초")

# # //////////////////////////////////////

# def check_time(func):
#     start = time.time()
#     func()
#     end = time.time()
#     print(f"수행 시간 : {end-start}초")
# def a():     
#     for i in range(10):   #100
#         print(i)
#         time.sleep(1)     #0.5
# check_time(a)

# /////////////////////////////////////////////

# start = time.time()

# for i in range(10):
#     print(i)
#     time.sleep(1)

# end = time.time()
# print(f"수행 시간 : {end-start}초")

# sys 모듈 
# import sys
# print(sys.argv)

# args = sys.argv[1:]
# print(args)

# print(int(sys.argv[1] + int(sys.argv[2])))

# ///////////////////////////////////
# import sys

# args = sys.argv[1:]
# print(args)

# total = 0
# for i in args:
#     total += int(i)
    
# print("합계", total)

# ////////////////////////////////
# import sys

# args = sys.argv[1:]
# val = 0
# for i in args:
#     if len(args) <= 2 or len(args) >= 4:
#         print("error")
#         break
#     if sys.argv[1] == "mul":
#         val = int(sys.argv[2]) * int(sys.argv[3])
#     elif sys.argv[1] == "add":
#         val = int(sys.argv[2]) + int(sys.argv[3])
# print(val)

# ////////////////////////////////////////////
# 다른 버전
# import sys

# args = sys.argv
# if (len(args) !=4):
#     print("입력오류")

# else:
#     cmd = args[1]
#     num1 = int(args[2])
#     num2 = int(args[3])
#     if cmd == "mul":
#         print(num1*num2)
#     elif cmd == "add":
#         print(num1+num2)

# /////////////////////////////////////////////
# sys. exit(0) 파이썬 프로그램 종료버튼

# ///////////////////////////////////////////////////
# sys.exit(0)으로 고쳐보기
# import sys

# args = sys.argv[1:]

# # 매개변수 길이 확인
# if len(args) != 3:
#     print("놉")
#     sys.exit(0)

# if args[0] == "mul":
#     val = int(args[1]) * int(args[2])
# elif args[0] == "add":
#     val = int(args[1]) + int(args[2])
# else:
#     print("놉")
#     sys.exit(0)

# print(val)
# sys.exit(0)

# 빈 배열에는 for 구문이 안된다.
# //////////////////////////////////////////
# OS 모듈
# import os

# os.chdir("C:/Users/g_gyuuuuuu/Desktop/python2")  # 내 깃 경로를 넣기, 역슬레시 슬레시 바꿔라.
# dir = os.popen("dir") # git status, dir 넣어보기
# print(dir.read())

# print(os.listdir())
# //////////////////////////////////////////////

# 타자 연습 게임
# import random
# import time

# word = ['sky', 'earth', 'moon', 'flower', 'tree', 'apple',
#         'grape', 'garlic', 'onion', 'potato']

# n = 1  # 문제 번호

# input("[타자 게임] 준비되면 엔터!")
# start = time.time()  # 시작 시간

# while n < 11:
#     print("문제", n)
#     question = random.choice(word)
#     print(question)  # 문제 출제
#     user = input()
#     if question == user:
#         print("통과!!")
#         n += 1  # 다음 문제 카운트
#     else:
#         print("오타! 다시 도전!")

# end = time.time()  # 종료 시간
# et = end - start
# print(f'타자 시간: {et:.2f}초')

# ////////////////////////////////////////////
# modules 폴더 만들고 그 폴더 안에 mylib 만들고 그 안에 food.py 파일 만듬.

# from modules.mylib import food # 컨트롤 클릭
# print(food.name)
# food.cook()
# food.eat  # food 파일에 있는 코드를 사용 가능. 예) 장금이 요리하다.

# from modules.mylib.food import cook, eat, name
# print(name)
# cook()
# eat()

# import bbb.cm2  # bbb는 또다른 파일 만들었을 때 사용.
# print(bbb.cm2.add(1,2))

# //////////////////////////////////////////////////////
# 9. 파일 입출력, 예외처리 시작

# 입,출력 스트림
# 스트림 : 자료흐름이 물의 흐름과 같다
# 입력 스트림, 자료를 읽을때 사용
# 출력 스트림, 파일에 저장할 때 사용

# f = open("file1.txt", "w") # 글자를 넣은 파일 생성
# f.write("hello world\n")
# f.close()  # 이거까지 해줘야 파일 안에 작성됨.

# f2 = open("file1.txt")
# print(f2.read(10)) # 숫자넣은만큼 읽는다. 1번부터 순번, 띄어쓰기 포함
# f2.close()

# f = open("file1.txt", "a")   # 추가된 파일 안에 글자 입력
# print(f.write("Hello world222\n"))
# f.close()

# readline 내용 배우기, 한번에 읽어오는 read와 한줄 씩 읽는 readline
# f2 = open("file1.txt")
# print(f2.read())
# f2.close()

# f3 = open("file1.txt")
# print(f3.readline(), end="")  # end 없을 때랑 다름
# print(f3.readline(), end="")
# print(f3.readline(), end="")
# f3.close()