# 실습 2, supermarket 클래스
# 조건) 클래스 선언 시, 인자로 locatrion,name, product, customer 받기
# location : 위치, name : 가게 이름, product : 파는 물건, customer : 고객의 수
# print_location() : 위치를 출력하는 함수
# change_category() : 받은 인자로 파는 물건 바꾸는 함수
# show_list() : 현재 파는 물건 출력
# enter_customer() : 손님의 수를 1씩 늘리는 함수
# show_info() : 가게 이름, 위치, 파는 물건, 손님 수 모두 출력
# show_supermarket_count() : 슈퍼마켓 클래스 인스턴스 개수 출력

# class Supermarket:
#     count = 0

#     def __init__(self, location, name, product, customer):
#         self.location = location
#         self.name = name
#         self.product = product
#         self.customer = customer
#         Supermarket.count += 1

#     def print_location(self):
#         print(f"위치 : {self.location}")

#     def change_category(self, new_product):
#         self.product = new_product
    
#     def show_list(self):
#         print(f"현재 파는 물건 : {self.product}")

#     def enter_customer(self):
#         self.customer += 1

#     def show_info(self):
#         print(f"가게 이름: {self.name}, 위치 : {self.location}, 파는 물건: {self.product}, 손님 수 : {self.customer}")
    
#     def show_supermarket_count():
#         print(f"전체 슈퍼마켓 개수: {Supermarket.count}")


# market1 = Supermarket("서울", "서울슈퍼", "과일", 10)
# market2 = Supermarket("부산", "부산슈퍼", "야채", 5)

# market1.print_location()

# market1.change_category("고기")
# market1.show_list()

# market2.enter_customer()
# market2.show_info()

# Supermarket.show_supermarket_count()


# 클래스 상속
# class Country:
#     def __init__(self):
#         self.name = "나라이름"
#         self.population="인구"
#         self.capital="수도"

#     def show(self):
#         print("국가 클래스의 메소드")

# class Korea(Country):
#     def __init__(self, name):
#         self.name = name

#     def show_name(self):
#         print("국가 이름:", self.name)

# country = Korea("대한민국")
# country.show()
# print(country.name)
# country.show_name()

# 부모꺼에 내꺼를 똑같이 덮어쓰는것

# 실습 3
# 다음과 같은 조건을 만족하는 MinLimitCalculator 클래스 만들기
# 1) Calculator 클래스를 상속받는다.
# 2) calue 값이 음수가 안되게 제한한다.
# 3) sub()메서드를 오버라이딩하여 2번 조건 만족시킬 것

# 부모 클래스 정의
# class Calculator:
#     def __init__(self):
#         self.value = 100  # 초기 값은 100으로 설정

#     def sub(self, value):
#         self.value -= value  # 값을 빼는 메서드

# # 자식 클래스 정의
# class MinLimitCalculator(Calculator):
#     def sub(self, value):
#         # 음수 제한을 추가하여 오버라이딩
#         if self.value - value < 0:
#             self.value = 0  # 음수가 되지 않도록 0으로 설정
#         else:
#             self.value -= value

# # 실행 코드
# cal = MinLimitCalculator()
# cal.sub(20)  # 100 - 20 = 80
# cal.sub(90)  # 80 - 90 -> 0 (음수 방지)
# print(cal.value)  # 출력: 0


# 8. 모듈 
# 모듈이란 
# 여러 기능들이 뭉쳐진 하나의 .py 파일
# 코드를 분리하고 공유하는 일
# 표준 모듈은 파이썬에 기본 내장, 외부 모듈은 직접 만든 모듈
# 예) 계산기 모듈, calc_module.py 파일 만들기

# 중간 내용은 다른 파일에 module 파일에 있음.

# 모듈에서 datetime, time 등등 이것들은 기본적으로 데이터를 제공해줌,


# import math
# print(math.floor(3.141592))       # math만
# print(math.ceil(3.141592))
# print(math.sqrt(9))

# from math import floor, ceil      #
# print(floor(3.141592))
# print(ceil(3.141592))

# 표준 모듈- random 모듈
# randint 정수
# uniform 실수
# random 0부터 
# randrange 

# import random  # 랜덤 게임 예시
# print(random.randint(1,5))
# print(random.uniform(1,5))   # 여기까지는 포함 가능
# print(random.random())       # 여기부터는 포함 불가능
# print(random.randrange(1,3))   
# print(random.randrange(1,5,2))

# up_and_down 게임, 최대 7번 안에 정답을 찾을 수 있는 게임.
# import random
# com = random.randint(1, 100)
# min_v = 1
# max_v = 100

# while True:
#     try:
#         guess = int(input("숫자 입력(%d ~ %d): " % (min_v, max_v)))
    
#         if guess < 1 or guess > 100:
#             print("입력 범위를 초과했어요")
#         elif com == guess:
#             print("정답이에요!")
#             break
#         elif com > guess:
#             print("랜덤수보다 작아요")
#             min_v = guess + 1
#         else:
#             print("랜덤수보다 커요")
#             max_v = guess - 1
#     except ValueError:
#         print("숫자만 입력 가능합니다.")

# 실습. 로또 번호 뽑기
# 1-45까지의 수 중에서 랜덤으로 6개의 숫자를 뽑는다.
# 6개의 숫자 중 중복되는 숫자가 없도록 한다.
# 오름차순 정렬한다.

# import random
# lotto = set()
# while len(lotto) < 6:
#     number = random.randint(1, 45)
#     lotto.add(number)
# print("로또 번호:", sorted(lotto))

# 로또 번호 뽑기 방법은 여러가지임.

# datetime 모듈, 날짜,시간
# import datetime

# now = datetime.datetime.today()
# print(now,"입니다.")
# print(now.year,"년 입니다.")
# print(now.month,"월 입니다.")
# print(now.day,"날 입니다.")
# print(now.hour,"시 입니다.")
# print(now.minute, "분 입니다.")
# print(now.second, "초 입니다.")

# print(f"{now.year}년 {now.month}월 {now.day}일 입니다.")
# print(f"{now.hour}시간 {now.minute}분 {now.second}초 입니다.")


# 지금까지 몇일 지났는지 세기
import datetime
print("지금까지 몇 일?")
first_day = datetime.date(2024, 11, 25)
print(first_day)

today = datetime.date.today()
print(today)

passed_time = today - first_day
print(passed_time)

print(f"개강 이후 {passed_time.days}일 지났습니다.")


