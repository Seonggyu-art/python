# a = 10
# b = 20
# print(a > b)  # False
# print(a == 10)  # True


# count = 1
# while count <= 5:
#     print(count)  # 1, 2, 3, 4, 5 출력
#     count += 1  # count 값을 1씩 증가
 

#  break 사용
# for i in range(1, 10):
#     if i == 5:
#         break
#     print(i)  # 1, 2, 3, 4 출력

# # # continue 사용
# for i in range(1, 10):
#     if i % 2 == 0:  # 나머지를 구하는 연산자.
#         continue
#     print(i)  # 홀수만 출력 (1, 3, 5, 7, 9)

# -------------------------------------------------------------------------------

# 1-4 공부 후 연습문제 풀어보기


# 문제 1: 리스트 생성하기
# 숫자 1, 2, 3, 4, 5를 포함하는 리스트를 만들어 출력하세요.
# list = [1, 2, 3, 4, 5]
# print(list)

# 문제 2: 리스트 값 수정
# 리스트 [10, 20, 30, 40, 50]에서 30을 300으로 바꿔서 출력하세요.
# list = [10, 20, 30, 40, 50]
# del list[2]    # 0부터 시작 
# list.append(300) # 맨 뒤에 추가
# list.sort()
# print(list)

# 정답
# list = [10,20,30,40,50]
# list[2] = 300      # 그자리에 넣기
# print(list)

# 문제 3: 짝수 출력하기
# 숫자 리스트 [1, 2, 3, 4, 5, 6]에서 짝수만 출력하세요.
# numbers =[1,2,3,4,5,6]
# for num in numbers:
#     if num % 2 == 0: # %는 나머지를 구할 때, 짝수 조건
#         print(num)

# 문제 4: 문자열 반복
# 문자열 "Python"을 3번 반복해서 출력하세요.
# a = ("python")
# b = (a * 3)
# print(b)

# 정답
# text = "python"
# print(text * 3)

# 문제 5: 조건문 사용하기
# 숫자 7이 짝수인지 홀수인지 확인하여 출력하세요.
# number = 7
# if number % 2 == 0:
#     print("짝수")
# else:
#     print("홀수")

# --------------------------------------------------------------------
# 문제 1: 리스트 값 추가
# 빈 리스트 my_list에 숫자 10, 20, 30을 순서대로 추가하고 출력하세요.
# my_list = []
# my_list.append(10)
# print(my_list)
# my_list.append(20)
# print(my_list)
# my_list.append(30)
# print(my_list)

# 문제 2: 리스트 길이 구하기
# 리스트 [5, 10, 15, 20, 25]의 길이를 구해 출력하세요.
# list = [5,10,15,20,25]
# print(len(list))

# 문제 3: 홀수와 짝수 개수 세기
# 숫자 리스트 [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]에서 짝수와 홀수의 개수를 각각 세어 출력하세요.
# numbers = [1,2,3,4,5,6,7,8,9,10]
# for num in numbers:
#     if num % 2 == 0:
#         print(len(num))
#     else:
#         print(len(num))
# # 틀림, 
# 홀수 조건 : num % 2 != 0
# 짝수 조건 : num % 2 == 0
# len()은 리스트 전체 길이를 반환하는 것으로 이 문제는 각 각의 개수이기에 맞지 않는다.
# even_count, old_count
# 정답
# numbers = [1,2,3,4,5,6,7,8,9,10]
# even_count = 0
# old_count = 0

# for num in numbers:
#     if num % 2 == 0:
#         even_count += 1
#     else:
#         old_count += 1
# print(f"짝수 개수 : {even_count}")
# print(f"홀수 개수 : {old_count}")

# 문제 4: 문자열 부분 출력
# 문자열 "Hello, Python!"에서 Python만 출력하세요.
# text = "Hello, python!"
# print(text[7:13])

# 문제 5: 특정 단만 출력
# 구구단 중 7단만 출력하세요.
# for i in range(1,10): # range는 1부터 9까지 반복함.
#     print(f"7 x {i} = {7 * i}")