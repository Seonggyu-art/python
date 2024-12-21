# 1220 4_반복문 복습

# i = 0
# while i < 5:
#     print("안녕", i)
#     i += 1

# # for문
# for i in range(1,6):
#     print(i)

# for i in range(0, 10, 2):
#     print(i)    


# break와 continue
# for i in range(10):   # 0부터 시작
#     if i == 5:
#         break
#     print(i)

# for i in range(10):
#     if i % 2 == 0:
#         continue  # 나온 부분은 건너뛰기, 홀수만 출력됨.
#     print(i)

# 이중 반복문
# for i in range(2,10):
#     for j in range(1,10):
#         print(f"{i} x {j} = {i*j}")
#     print() # 띄어쓰기를 위한 프린트임.

 # 예시 문제 1
# for i in range(1,11):
#     print(i)
#     i += 1

# 문제 2
# for i in range(1, 21):
#     if i % 2 == 0:
#         print(i)

# 문제 3
# sum = 0
# for i in range(1, 101):
#    sum += i
# print(f"1부터 100까지 합: {sum}")

# 문제 4
# i = int(input("숫자 2~9까지 입력하세요"))
# for j in range(1,10):
#     print(f"{i} x {j} = {i*j}")

# 문제 5
# for i in range(1,6):
#     print("*"*i)

# 문제 6
# sum = 0
# li = [90, 85, 70, 75, 95]
# for i in li:
#     sum += i
# print(f"li의 합계 : {sum}")
# print({sum/len(li)})

# 문제 7
# while True:
#     num = int(input("숫자 입력해"))
#     if num == -1:
#         print(" 종료")
#         break
#     print(f"입력한 번호 : {num}")

# 리스트 합
# sum = 0
# list = [5, 10, 15, 20, 25]
# for i in list:
#     sum += i
# print(f"리스트의 함 : {sum}")

# 1부터 n까지의 짝수 합
# num = int(input("입력 받을게 짝수 값만 내놔"))
# for i in range(2,num,2):
#     print(f"짝수 합: {i}")

# 1부터 n까지의 짝수 합
# num = int(input("번호 줘"))
# sum = 0
# for i in range(1, num):
#     if i % 2 == 0:
#         sum += i
# print(f"짝수 합 : {sum}")

# 리스트에서 3의 배수 개수 세기
# A = 0          # count, 수세기
# list = [ 4, 9, 12, 15, 22, 33]
# for i in list:
#     if i % 3 == 0:
#         A += 1
# print(A)

# 리스트에서 최댓값값 위치 찾기
# list = [23, 45, 12, 67, 34]
# print(list.index(67))
# maxi = max(list)
# index = list.index(maxi)       # index는 사용할 때 앞에 .을 쓰기, 리스트에서 사용가능능
# print(f"최댓값 : {maxi}, 위치 : {index}")

# 리스트 최솟값과 위치 찾기
list = [18,7,42,15,3,39]
print(min(list))
print(list.index(3))

# 특정 값의 등장 횟수
list = [4, 7, 4, 9, 4, 11, 4, 5]
