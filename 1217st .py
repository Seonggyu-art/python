# 12월 17일 파이썬 복습
# 슬라이싱

# 기본 슬라이싱
# numbers =[1,2,3,4,5,6,7,8,9,10]
# print(numbers[1:5]) # 출력 [2,3,4,5]
# [0번부터 : 1번부터]

# 처음부터 가져오기
# print(numbers[:4]) # 출력 [1,2,3,4]
# [처음부터 하고 싶으면 생략 : 1번부터]


# 끝까지 가져오기
# print(numbers[3:]) # 출력 [4,5,6,7,8,9,10]
# [0번부터 : 끝까지하고 싶으면 생략략]

# 간격 지정
# print(numbers[::2])  # 출력 [1,3,5,7]
# [:: 2 간격이고 0부터 시작]

# 역순으로 가져오기
# print(numbers[::-1]) # 출력 [10,9,8,7,6,5,4,3,2,1]
# [::-1] 리스트를 역순으로 시작함.-1이 시작

# numbers = [1,2,3,4,5]
# print(numbers)
# print(numbers[0])
# print(numbers[2])
# print(numbers[0:3])
# print(numbers[::2])
# print(numbers[::-1])

# num = int(input("숫자를 입력해"))
# print(num)
# print(num + 10)
# num1 = int(input("두번째 숫자"))
# print(num +num1)
# if num % 2 == 0:
#     print("쨕수")
# else:
#     print("홀수")
# if num >10:
#     print("10보다 큼")
# else:
#     print(" 작아")

# num = int(input("숫자 입력해라라"))
# print(num)

# num = int(input("숫자를 입력하세요: "))
# print("결과", num+ 10)

# num1 = int(input("첫 번째 숫자 입력해라 :"))
# num2 = int(input("두 번째 숫자를 입력하세요: "))
# print(num1 + num2)

# num = int(input(" 숫자 :"))
# if num % 2 == 0:
#     print(" 짝수")
# else:
#     print(" 홀")

# numbers =[1,2,3,4,5,6,7,8,9,10]
# for num in numbers:
#     if num % 2 == 0:
#         print(num)

# numbers =[1,2,3,4,5,6,7,8,9,10]
# print(numbers[:3])
# print(numbers[3:6])
# print(numbers[::2])

# numbers =[1,2,3,4,5,6,7,8,9,10]
# for num in numbers:
#     if num%3 == 0:
#         print(num)

# numbers =[1,2,3,4,5,6,7,8]
# result =[num *2 if num % 2 ==0 else num for num in numbers]  
# print(result)   

# numbers =[1,2,3,4,5,6,7,8]
# result = []

# for num in numbers:
#     if num % 2 == 0:
#         result.append(num*2)
#     else:
#         result.append(num)
# print(result)

# numbers = [2, 3, 6, 8, 12, 15, 18, 20, 24]
# result = []

# for num in numbers:
#     if num % 3 == 0 and num % 2== 0:
#         result.append(num)
# print(result)

# result = [num for num in numbers if num % 3 ==0 and num % 2 ==0]
# print(result)

# numbers = [10, 20, 30, 40, 50]
# result = sum(numbers)
# print("합: ", result)

# numbers = [15, 22, 8, 37, 11, 5, 29]
# max_num = max(numbers)
# min_num = min(numbers)
# print("최댓값", max_num)
# print("최소", min_num)
# print("최댓값",max(numbers))@@@@@@@@@@

# numbers = [10, 15, 20, 25, 30, 35, 40]
# list = []

# for num in numbers:
#     if num % 2 == 0:
#         list.append(num)
# print(list)

# numbers = [1, 2, 3, 4, 5, 6, 7, 8]
# print(numbers[2:6])

# numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# result =[num *2 if num % 2 ==1 else num/2 for num in numbers]  
# print(result[2::])

# numbers = [[1, 2], [3, 4], [5, 6]]
# print(numbers[0]) # 첫번째 서브 리스트를 뽑기
# 첫번째 서브 리스트를 뽑기 위해서는 0번부터 시작함.

# print(numbers[1][1]) # 서브리스트 안에 서브리스트 뽑기기

# numbers = [[1, 2], [4, 5], [3, 6], [8, 9], [7, 10]]
# result =[]

# for num in numbers:
#     if num[0] % 2 == 0:
#         result.append(num[1]*3)
# print(result)

# numbers = [[1, 2], [4, 5], [3, 6], [8, 9], [7, 10]]
# result =[]

# for num in numbers:
#     if num[0] % 2 == 1:
#         result.append(num[1]*2)
# print(result)

# numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# result =[]

# for num in numbers:
#     if num % 2 == 1:
#         result.append(num*2)
#     else:
#         result.append(num/2)
# print(result[2::])

# numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# result = [num*2 if num % 2 == 1 else num / 2 for num in numbers]
# print(result[2::])

# numbers = [2, 3, 5, 6, 9, 10, 12, 15, 18, 20, 24]
# result = []

# for num in numbers:
#     if num % 3 == 0:
#         num = 2*num
#     elif num % 5 == 0:
#         num =num/2

#     if num > 10:
#         result.append(num)
# print(result)

# numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# result = []

# for num in numbers :
#     if num % 2 == 0:
#         num = 2*num
#     else:
#         num = 3*num

#     if num > 20:
#         result.append(num)

# print(result)

# numbers = [10, 15, 20, 25, 30, 35, 40]
# result = []

# for num in numbers:
#     if num % 2 == 0:
#         result.append(num)

# print(sum(result))

# numbers = [10, 15, 20, 25, 30, 35, 40]
# asum = sum(num for num in numbers if num %2 ==0)
# print(asum)

# range(start, stop, step)
# start : 포함
# stop : 포함 안됨. 예 11이라고 하면 11에 멈추는 거임.
# step : 간격, 기본은 1

# for num in range(1,11): # 출력 1부터 10까지 숫자 발생
#     print(num)
# range( 1부터 시작이고, )

# for i in range(1,21):
#     if i % 2==1:
#         print(i)

# for i in range(1, 21, 2):
#     print(i)

# for i in range(10,0, -1):
#     print(i)

# num = sum(range(1,11))
# print(num)

# i = list(range(5, 51, 5))
# print(i)

# for i in range(1,101):
#         if i % 3 == 0 and i % 5 ==0:
#                 print(i, end=" ") 
# print를 할 때, end=""를 사용하면 가로 한줄쓰기로 가능능
            
# 문제 2번부터 풀기기



# 문제 리스트 슬라이싱 연습하기
# 정수 n을 입력 받아 1부터 n까지의 정수를 포함하는 리스트를 만들어라
# 슬라이싱을 사용해, 홀수와 짝수만 출력

# num = int(input("정수를 입력해: "))
# lis = num
# for list in num:
#     if list % 2 == 0:
#         print("짝수", num)
#     else:
#         print("홀수", num)


# numbers = [[1, 2], [3, 4], [5, 6], [7, 8], [9, 10]]
# result = []

# for i in numbers:
#     if i[0] % 2 == 1:
#         list = i[1]*3
#     if list >= 15:
#         result.append(list)
# print(result)

# numbers = [[5, 6], [15, 20], [8, 10], [20, 15], [25, 30]]
# result = [5*i[1] for i in numbers if i[0] > 10 and i[1] % 2 == 0 ]
# print(result)

# result = []
# for i in numbers:
#     if i[0] > 10 and i[1] % 2 == 0:
#         result.append(i[1]*5)
# print(result)

# 정수 n을 입력 받아 1부터 n까지의 정수를 포함하는 리스트 만들기
# n = int(input("입력을 해주세요"))
# numbers = list(range(1, n + 1))  # n+1까지 하기 전에 종료.
# print(numbers)

# 슬라이싱을 사용해서 홀수, 짝수만 출력하기
# n = int(input(" 정수를 입력해해"))
# numbers = list(range(1, n+1))
# a = numbers[]

# 리스트[시작인덱스:끝인덱스:간격]
# numbers[::2] # 홀수만을 슬라이싱 하는 법
# numbers[1::2] # 짝수만을 슬라이싱 하는 법

ab = ["ㄱ", "ㄴ", "ㄷ"]
n = input("마시고 싶은 음료는?")  # int 숫자(정수만)를 반영함. 그러지 않으면 사용안함.
if n in ab:
    print(f"{n} 드릴게요.")
else:
    print(f"{n}은 없습니다.")



