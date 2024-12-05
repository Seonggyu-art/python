# # 2차원 리스트, 구구단 3단 만들기, 5개
# for x in range(1,10):
#     print(f"3 x {x} = {3 * x}")

# d = {x: 3 * x for x in range(1,10)}
# for x, y in d.items():
#     print(f"3 x {x} = {y}")

# d = [(x, 3 * x) for x in range(1, 10)]
# for x, y in d:
#     print(f"3 x {x} = {y}")

# d = [
#     [3,1],
#     [3,2],
#     [3,3],
#     [3,4],
#     [3,5],
#     [3,6],
#     [3,7],
#     [3,8],
#     [3,9],
#     ]
# for x,y in d:
#     print(f" {x} x {y} = {x*y}")

# d = [
#     [3,1],
#     [3,2],
#     [3,3],
#     [3,4],
#     [3,5],
#     [3,6],
#     [3,7],
#     [3,8],
#     [3,9],
#     ]
# for i in d:
#     print(f"{i[0]} * {i[1]} = {i[0]*i[1]}")

# # 함수 만들기
# def f(x):
#     result = x**2 + 2*x + 1
#     return result
# print(f(3))

# # 그저 함수 내부의 일만 수행
# def sayHi():
#     print("Hi")
#     print("Hi")
#     print("Hi")
# sayHi()

# #구구단을 출력하는 함수
# def print_gugudan(dan):
#     for i in range(1,10):
#         print(dan, 'x', i, '=', (dan * i))
# print_gugudan(5)

# #변수범위 예
# x = 10 #전역변수
# def func():
#     x = 20 #지역변수
#     print(x)

# func()
# print(x)

# def func2():
#     print(x)
# func2 

# def func3(x): #지역변수
#     print("func3", x) #지역변수
# func3(3)

# #실습 1, 두 수(2,2)를 매개변수 전달하여 서로 같으면 곱, 다르면 더하는 함수를 정의
# # 호출하는 프로그램을 작성해라
# def calculate(a, b):
#     if a == b:
#         return a * b
#     else:
#         return a + b
# result1 = calculate(2,2)
# print("결과(곱) :", result1)

# result2 = calculate(2,3)
# print("결과(합) :",result2) 


# def func(x,y) :
#     if x == y :
#         print(x*y)
#     else :
#         print(x + y)

# func()  
# func(5,3)

# 실습 2, 주문 상품가격이 이만원 미만이며 배송비 2500원 포함, 아니면 배송비를 포함하지 않는 프로그램
# 배송비 계산하기
# def func(price_per_item, qt):
#     total_price =price_per_item * qt
#     if total_price < 20000:
#         total_price += 2500
#     print(f"상품 가격 : {format(total_price, ',')}원")

# func(30000, 1)
# func(17500, 1)


# def func(x, y):
#     if (x*y) >= 20000:
#         val = x * y
#     else:
#         val = x * y+2500

#     return val
# a = int(input("상품 금액 입력: "))
# b = int(input("상품 수량 입력: "))
# print(f"총 가격 : ", func(a,b))

# #리스트를 매개변수로 새로운 리스트 만들기
# def times(l):
#     l2 = [i*2 for i in l]
#     return l2 # 여기에서 return set(l2) 하면 결과값{}으로 나옴.

# v2 = times([1,2,3,4,5])
# print(v2)


# def sum_mul(a,b):
#     sum = a+b
#     mul = a*b
#     return sum, mul

# s, m = sum_mul(2,3)
# print(s, m)

# #실습3 자판기 프로그램 함수화
# drink_list = ['게토레이', '게토레이', '레쓰비', '레쓰비', '생수', '생수', '생수', '이프로']

# def check_machine():
#     print(f"\n남은 음료수 : {drink_list}")

# def is_drink(drink):
#     if drink in drink_list:
#         return True
#     else:
#         return False

# def add_drink(new_drink):
#     drink_list.append(new_drink)
#     print(f"\n{new_drink}가 추가되었습니다.")

# def remove_drink(drink):
#     if is_drink(drink):
#         drink_list.remove(drink)
#         print(f"\n{drink}가 제거되었습니다.")
#     else:
#         print(f"\n{drink}가 목록에 없습니다.")

# def vending_machine():
#     check_machine()
#     role = input("\n사용자 종류 선택:\n1. 소비자\n2. 주인\n입력: ").strip()
    
#     if role == "1":
#         drink = input("\n 마시고 싶은 음료를 선택해").strip()
#         if is_drink(drink):
#             remove_drink(drink)
#             print(f"\n{drink}를 줄게요.")
#         else:
#             print(f"\n{drink}가 없습니다.")
#     elif role == "2":
#         action = input(f"\n작업을 선택하세요.:\n1. 추가\n2. 삭제\n입력 :").strip()
#         if action == "1":
#             new_drink = input("\n추가할 음료 이름 입력: ").strip()
#             add_drink(new_drink)
#         elif action == "2":
#             drink = input("\n삭제할 음료 이름 입력: ").strip()
#             remove_drink(drink)
#         else:  # 잘못된 작업 선택
#             print("\n잘못된 작업 선택입니다.")
#     else:  # 잘못된 사용자 입력
#         print("\n잘못된 입력입니다. 1 또는 2를 선택해주세요.")

#     check_machine()
# vending_machine()

# 실습 4, 정수를 저장하는 스택을 구현, 입력으로 주어지는 명령을 처리하는 프로그램 작성
import sys

# 스택 초기화
stack = []

# 스택 명령 함수들
def push(p):
    stack.append(p)

def pop():
    if len(stack) == 0:
        print(-1)
    else:
        print(stack.pop())

def size():
    print(len(stack))

def empty():
    if len(stack) == 0:
        print(1)
    else:
        print(0)

def top():
    if len(stack) == 0:
        print(-1)
    else:
        print(stack[-1])

# 입력 처리
line = int(sys.stdin.readline())  # 명령어 개수 입력받음

for _ in range(line):
    func = sys.stdin.readline().split()  # 명령어 입력받음
    if func[0] == 'push':
        push(int(func[1]))
    elif func[0] == 'pop':
        pop()
    elif func[0] == 'size':
        size()
    elif func[0] == 'empty':
        empty()
    elif func[0] == 'top':
        top()
