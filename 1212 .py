# 파일 입출력
# f4 = open("file1.txt")
# print(f4.readlines())
# f4.close()

# seek(위치)

# f5 = open("file1.txt", "r+")
# print(f5.read())
# print(f5.tell())
# f5.seek() # 특정 위치로 이동하는 것
# print(f5.read())
# f5.close()

# file1에서 5를 8로 변경하고 싶을 때
# f5 = open("file1.txt", "r+")
# print(f5.read())
# print(f5.tell())
# f5.seek(4) # 특정 위치로 이동하는 것
# print(f5.write("8"))
# f5.close()         #이렇게 하면 12345678, 8, 1 이 나오는데, 1은 몇개를 반환했는지 알려주는 거

# with -as 구문
# fi.close()를 사용하지 않아도 되는거
# with open("file1.txt", 'r+')as f7:
#     str6 = f7.read()
#     print(f7.tell())
#     f7.seek(str6.find('4'))
#     print(f7.read())

# 이차원 리스트 만들기
# 많이 중요하진 않음. 

# 영어 타자 게임
# import random

# with open("word.txt", 'w') as f:
#     # 컨트롤 시프트 f 누르면 그동안 했던 내용 찾기 가능
#     word = ['sky', 'earth', 'moon', 'flower', 'tree', 'apple',
#         'grape', 'garlic', 'onion', 'potato']
#     for i in word:
#         f.write(i + ' ') # '\n', \t, \r

# with open ("word.txt", 'r') as f:
#     #data = f.readline().split() # \n인 경우에 이렇게도 가능
#     data = f.read().split()
#     word = random.choice(data)
#     print(word)

# /////////////////////////////////////////////

# import random
# import time

# with open("file1.txt", 'r') as f:
#     # 컨트롤 시프트 f 누르면 그동안 했던 내용 찾기 가능
#     # word = ['sky', 'earth', 'moon', 'flower', 'tree', 'apple',
#     #     'grape', 'garlic', 'onion', 'potato']
#     word = f.read().split()

# n = 1 # 문제
# input("[타자게임] 준비되면 엔터!")
# start = time.time()

# while n < 11:
#     print("문제",n)
#     question = random.choice(word)
#     print(question)
#     user = input()
#     if question == user :
#         print("통과!")
#         n += 1
#     else:
#         print("오타! 다시 도전!")

# end = time.time()
# et = end - start
# print(f"타자 시간: {et: .2f}초")

# 특정 파일이 있는지 알아보기 위해서는 os를 사용해야함. 
# import random
# import time
# import os

# if os.path.exists("word.txt"):
#     with open("word.txt", 'r') as f:
#         word = f.read().split()
# else :
#     word = ['sky', 'earth', 'moon', 'flower', 'tree', 'apple',
#         'grape', 'garlic', 'onion', 'potato']
    
# n = 1

# input("[타자 게임] 준비되면 엔터!")

# ////////////////////////////////////////////////////

# 다른 파일에 입력해 저장시키기
# try:

#     with open ("./output/input.txt", "a") as f:
#         while True:
#             text = input("저장할 내용 입력(종료-z)")
#             if text == 'z' or text == 'z':
#                 break
#                 #sys.exit(0)
#             f.write(text + '\n')
# except:
#     print('파일을 찾을 수 없습니다.')

# ////////////////////////////////////

# 실습 1. 회원 명부 작성하기
# 사용자에게 3명의 회원에 대한 이름 비밀번호 입력받기
# 사용자로부터 입력된 정보를 member.txt에 기록 (파일 쓰기모드)
# member.txt에 저장된 회원명부 출력(파일 읽기모드)

# 회원 명부 작성 프로그램

# with open("./member.txt", 'w') as f:
#     for i in range(3):
#         name = input("이름 입력: ")
#         password = input("비밀번호 입력: ")
#         f.write(name + password + '\n')  # 이러면 이름과 비밀번호가 헷갈릴 수 있어서. 다르게 해야함

# with open("./customer.txt", 'r') as f:
#     print(f.read().split())
#
#  ///////////////////////////////////////////////////

# 실습 2. 회원 명부를 이용한 로그인 기능
# 사용자에게 "이름을 입력하세요" 라는 메세지를 출력한 뒤 이름 입력받기
# 사용자에게 "비밀번호 입력하세요" 라는 메세지를 출력한 뒤 비번 입력받기
# member.txt에서 한 줄씩 "이름"과 "비번"을 검사하여 로그인 성공 시 "로그인 성공" 
# 실패시 "로그인 실패" 출력
# 여기서 member.txt 앞 실습에서 만든 회원 명부

# name = input("이름을 입력해라.")
# password = input("비밀번호 입력해라.")

# with open("./member.txt", 'r') as f:
#     word =" 로그인 실패"
#     for line in f:
#         n, p = line.split()

#         if n == name and p == password:
#             word = "로그인 성공"
#             break

# print(word)

# /////////////////////////////////////

# 다른 버전
# dictUser = {}

# with open("member.txt", 'r') as f:
#     for line in f:
#         n, p = line.split()
#         dictUser[n] = p

# print(dictUser)

# # for i in range(100) :
# name = input("이름을 입력하세요: ")
# pw = input("비밀번호를 입력하세요: ")

# if pw == dictUser.get(name):
#     print("로그인 성공!")
# else:
#     print("로그인 실패!")

# //////////////////////////////////////////////////

# 실습 3. 로그인 성공시 전화번호 저장하기
# 로그인 성공 시, 사용자에게 "전화번호를 입력" 라는 메세지를 출력한 뒤 전화번호 입력받기
# 사용자로부터 입력 받은 전화번호를 이름과 함께 member_tel.txt에 기록
# 새로운 사람이 로그인 성공 시 member_tel.txt에 전화번호 추가
# member_tel.txt에 이미 존재하는 사람이 로그인 성공 시 전화번호 수정

# 로그인 데이터 로드
dictUser = {}
try:
    with open("member.txt", 'r', encoding='utf-8') as f:  # 인코딩 추가
        for line in f:
            name, pw = line.strip().split()
            dictUser[name] = pw
except FileNotFoundError:
    print("member.txt 파일이 없습니다.")

# 로그인
name = input("이름을 입력하세요: ")
pw = input("비밀번호를 입력하세요: ")

if pw == dictUser.get(name):
    print("로그인 성공!")
    # 전화번호 저장
    phone = input("전화번호를 입력하세요: ")
    with open("member_tel.txt", 'a', encoding='utf-8') as f:  # 인코딩 추가
        f.write(f"{name}, {phone}\n")
    print(f"{name}님의 전화번호가 저장되었습니다.")
else:
    print("로그인 실패!")

            
            
    








