#while 문
# i = 0
# while i<5:
#     i+=1
#     print(i)
# print("끝")

#홀수만 출력하는 법
# i = 1
# while i <10:
#     print(i)
#     i +=2
# print('끝')

#실습1
#1부터 사용자가 입력한 수까지 정수의 합 계산
# for i in range(1,11):
#     print(i, end=' ') #1-10까지 나열

# sum_val = 0
# for i in range(1,11):
#     sum_val += i
# print(f'\n합계: {sum_val}') #합계: 값

# sum_val =0
# for i in range(1,11,2):
#     print(i, end=' ') #홀수 나열
#     sum_val += i
# print(f'\n합계: {sum_val}') #홀수 합계

#실습2
# 입력한 숫자만큼 카운트하고 "발사"출력
# n = int(input("정수를 입력"))

# for i in range(n, 0, -1):
#     print(i,end=" ")
# print("발사!")

# #실습3
# a = int(input('구구단을 외자'))
# for j in range(1,10):
#     print(f'{a} * {j} = {a*j}')

# a = [10,20,30]
# print(sum(a)/len(a))
# sum= 0
# for i in a: 
#     sum +=i
#     print(sum)

# a = [1,2,3,4,5]
# a2 =[]
# a3 =[]
# a4 =[]

# a3 =[i*3 for i in a]
# print(a3)

# a4 = [i*3 for i in a if i%2==0]
# print(a4)

# #이중 for문 외부/내부 반복문
# for y in range(3): # 외부
#     for x in range(2): #내부
#         print(f'y:{y}, x:{x}') #내부
#     print() #외부

# #이중 for문- 구구단 전체
# for i in range(2,10):
#     print(f'[{i}단]')
#     for j in range(1,10):
#         print(f'{i} X {j} = {i*j}')
#     print()

# #자리배치도
# print('*** 자리배치도 ***')
# customer = int(input('고객수 입력 : '))
# column = int(input('좌석열 수 입력: '))

# if customer % column ==0:
#     row = customer // column
# else:
#     row = (customer // column) +1

# for i in range(0, row):
#     for j in range(1, column + 1):
#         seat = i *column + j
#         if seat > customer:
#             break
#         ptint(seat, end=" ")
#     print("끝")



# 고객 수와 좌석행을 입력받아서 이쁘게 자리배치하기
# print("*** 자리 배치도 ***")

# # 고객 수와 좌석 행(row) 수 입력받기
# customer = int(input("고객 수 입력 :"))
# row = int(input("좌석 행 수 입력 : "))

# if customer <= 0 or row <= 0:
#     print("고객 수와 좌석 행 수는 1 이상이어야 한다.")
#     exit()

# # 열(column)수 계산
# if customer % row == 0:
#     column = customer // row
# else:
#     column = (customer // row) + 1

# #자리 배치 출력
# for i in range(row):
#     for j in range(1, column +1):
#         seat = i* column +j
#         if seat > customer:
#             break
#         print(f"{seat:3}", end=" ")
#     print()# 행 바꾸기

# print("\n자리배치가 완료되었습니다.")


# 실습4
# #1.  왼쪽정렬 별트리 만들기
# print(" 왼쪽 정렬 별 트리 만들기 ")
# n = int(input("별 트리 몇층? "))
# for i in range(1, n + 1):
#     print("*" * i)

# #2. 오른쪽 정렬 별트리 만들기
# print(" 오른쪽 정렬 별 트리 만들기 ")
# n = int(input("별 트리 몇층? "))
# for i in range(1, n + 1):
#     print(" " * (n - i) + "*" * i)

# #3. 중앙 정렬 별 트리 만들기
# print(" 중앙 정렬 별 트리 만들기 ")
# n = int(input("별 높이 몇층?"))
# for i in range(1, n + 1):
#     print(" " * (n - i) + "*" * (2 * i - 1))

# 실습 5
# 리스트 평균 구하기
# print("리스트 평균 구하기")
# ns_input = input("숫자 입력 칸") #여러 개의 숫자 받기
# ns_list = ns_input.split() # 공백 지우기
# ns = [int(n) for n in ns_list] #문자열을 정수로 변환

# print(ns) # 리스트를 출력

# max_n = max(ns) # 제일 큰 수와 작은 수를 찾고
# min_n = min(ns)

# print(f"가장 큰 값 : {max_n}") 
# print(f"가장 작은 값 : {min_n}")

# ns.remove(max_n) # 그 두 개를 뺀 나머지 값들의 평균 구하기
# ns.remove(min_n)

# if len(ns)> 0:
#     averge = sum(ns) / len(ns)
#     print(f"나머지 값의 평균 {averge}")
# else:
#     print("나머지 값이 없음")