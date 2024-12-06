# #함수의 기본 매개변수
# def pr_str(txt, count=1):
#     for i in range(count):
#         print(txt)

# pr_str("Hello",3)
# print()
# pr_str("Hello")

# """"""""""""""""""""""""""""""
# def pr_str(txt, count=1,count2=1):
#     for i in range(count):
#         print(txt)
#         print(count2)

# pr_str("Hello", 3, 2)
# pr_str("Hello",3)
# print()
# pr_str("Hello")
# print()

# """"""""""""""""""""""""
# def calc_avg(numbers):
#     print(type(numbers))
#     return sum(numbers)/len(numbers)

# print(calc_avg((1,2)))
# print(calc_avg((1,2,3,4,5)))

# """"""""""""""""""""""""""""""""""""
# def a():
#     return 1,2

# print(a())

# """"""""""""""""""""""""""""""""""""
# 함수의 가변 키워드 매개변수
# def introduce(**kw):
#     print(type(kw))
#     for k, v in kw.items():
#         print(f"{k}, {v}")
#     for i in kw:
#         print(f"{i}")

# introduce(name="Alice", age =25, city ="NY")

# """""""""""""""""""""""""""""""""""""""""
# list = [2,4,1,4,6]
# list.sort()
# print("list", list)
# list2 = [2,4,1,4,6]
# print("sorted list2", sorted(list2))
# print("list2", list2)

# """"""""""""""""""""""""""""""
# 3번째로 작은 값의 인덱스를 구하라.
# 정렬하고 그 값을 원본에서 찾으면 된다.

# """"""""""""""""""""""""""
# print(eval("1+2*2"))

# 반올림 반내림 하는 법
# print(int(4.6+0.5))
# print(int(4.4+0.5))
# print(round(4.6))
# print(round(4.4))
# """""""""""""""
# # 재귀함수
# def hello():
#     global count
#     if count == 3:
#         return
#     print("hello")
#     count += 1
#     hello() # 이게 자기 자신 호출

# count = 0
# hello("안녕")
# """""""""""""""""""""""""""
# # 실습 2, 방법 1 재귀 함수로 피보나치 수 구하기
# def fibo(n):
#     if n <= 2:  # F1, F2는 1
#         return 1
#     else:
#         return fibo(n - 2) + fibo(n - 1)

# # 테스트
# print(fibo(10))   # 5번째 피보나치 수
# print(fibo(15))  # 15번째 피보나치 수

# 방법 2, 메모제이션 활용하기
# memory = {1: 1, 2: 1}

# def fibo_memoization(n):
#     if n in memory:
#         number = memory[n]
#     else:
#         number = fibo_memoization(n-1) + fibo_memoization(n-2)
#         memory[n] = number
#     return number
# print(fibo_memoization(1))
# print(fibo_memoization(2))
# print(fibo_memoization(3))
# print(fibo_memoization(4))
# print(fibo_memoization(5))
# print(fibo_memoization(6))
# """"""""""""""""""""""""""""""""""""
# # 람다식 사용 예시
# add = lambda x,y:x+y
# print(type(add))
# print(add(1,2))

# def add2(x,y):
#     return(x+y)

# add3 = add2
# print(add2(1,2))
# print(add3(1,2))

# """"""""""""""""""
# # 이러한 형태를 주로 사용함

# def call_3(func):
#     for i in range(3):
#         func()

# call_3(lambda:print("hi")) # 콜백 함수
# call_3(lambda:(print("hello")))

# """"""""""""""""""""""""""""""""""""
# def download(startedcallback, endedcallback):
#     startedcallback()
#     print("download 중")
#     endedcallback()
# download(lambda:print("다운로드 시작"), lambda:print("완료되었습니다."))

# # """""""""""""""
# list(map(int, ["1","2","3"]))

# result = map(lambda x:3*x, [1,2,3,4])
# print(list(result))

# """"""""""""""""""""""""""""""""""""""""""
# 1보다 작은 함수를 만들 때? 람다함수 활용
# li = [-5, 1,2,-11, 76]

# value = list(filter(lambda x:x<0, li))
# print(value)
# value = list(filter(lambda x:x>10, li))
# print(value)
#""""""""""""""""""""""""""""""""""""""""""""""
# 연습문제, li에서 두배를 만들고 3이상인 것을 한줄로 출력해라
# li = [-5, 1, 2, -11, 76]
# print(list(filter(lambda x:x>=3, map(lambda x : 2 * x, li))))


#""""""""""""""""""""""""""""""""""""""""""
#  복습
# 정수 배열 arr 주어지고 arr의 각 원소에 대해 값이 50보다 크거나 같은 짝수라면
# 2로 나누고, 50보다 작은 홀수라면 2를 곱한다. 그 결과인 정수 배열을 
# return 하는 solution 함수 완성하기
# def solution(arr):
#     answer = []
#     for num in arr:
#         if num >= 50 and num % 2 == 0:
#             answer.append(num // 2)
#         elif num < 50 and num % 2 == 1:
#             answer.append(num * 2)
#         else:
#             answer.append(num)
#     return answer

# 문자열 mystring이 주어지고, mystring을 문자 "x"를 기준으로 나눴을 때
# 나눠진 문자열 각각의 길이를 순서대로 저장한 배열을 return 하는 solution 함수 완성
# def solution(myString):
#     parts = myString.split("x") 
#     print("split parts:", parts) # 중간 출력 확인
#     lengths = [len(part) for part in parts]
#     print("Lengths:",lengths) #중간 출력 확인
#     return lengths
# myString = "oxoxoxxox"
# print(solution(myString))

# 어떤 문자열 A가 다른 문자열 B안에 속하면 A를 B의 부분 문자열이라고 함.
# 예를 들어 문자열 "abc"는 "aabcc"의 부분 문자열이다.
# 문자열 str1과 str2가 주어질 때, str1이 str2의 부분 문자열이라면 1을
# 부분 문자열이 아니라면 0을 return하도록 solution 함수 완성하기
# def solution(str1, str2):
#     # str2가 str1에 포함되어 있는지 확인
#     if str2 in str1:
#         return 1  # 포함되어 있으면 1 반환
#     else:
#         return 0  # 포함되어 있지 않으면 0 반환

# # 테스트 입력
# str1 = "ab6CDE443fgh22iJKlmn1o"
# str2 = "6CD"
# print(solution(str1, str2))  # 출력: 1

# str1 = "ppprrrogrammers"
# str2 = "pppp"
# print(solution(str1, str2))  # 출력: 0





