# 2. 리스트와 조건문 복습하기

# fruits = ['사과', '바나나', '포도', '딸기']
# print(fruits[0])

# fruits.remove("사과")
# fruits.append("이구아나")
# print(fruits)

# if "사과" in fruits:
#     print(" 사과 여깄다.")
# else:
#     print("없음요")

# /////////////////////////////
# 문제 1번 리스트 생성
# numbers = [10,20,30,40,50]
# print(numbers[0:3])

# # 문제 3
# numbers[1] = 25
# print(numbers)

# # 문제 4
# print(len(numbers))

# # 문제 5
# if numbers[2] >= 30:
#     print("30이상")
# else:
#     print("아님님")

# /////////////////////////

# 문제 1
# fruits = ["사과", "바나나", "포도", "딸기", "오렌지"]
# for fruit in fruits:
#     print(fruit)

# # 문제 2 ?>>>?
# numbers = [5, 10, 15, 20, 25]
# total = 0
# for number in numbers:
#     total += number
# print(total)

# 문제 3  ?>>>?
# numbers = [3, 7, 12, 5, 10, 18, 2]
# numbers = [num for num in numbers if num > 10]
# print(numbers)

# # 문제 4
# A_list = [["사과","포도"], ["바나나","딸기"], ["오렌지", "키위"]]
# print(A_list[1][0])

# 문제 5
# numbers = [1,2,3,4,5]
# for num in numbers:
#     if num % 2 == 0:
#         print("짝수")
#     else:
#         print("홀")

# //////////////////////////////

# 문제 1
# numbers =[18,34,12,56,7,23,45]
# print(min(numbers))

# 문제 2
# names = ["영희", "민수", "지영"]
# names.insert(2,"철수")
# print(names)

# 문제 3
# colors =["빨강", "파랑", "노랑", "초록"]
# removed_color = colors.pop(3)
# print(removed_color)

# 문제 4, 인덱스는 0123 지칭함함
# names = ["영희", "철수", "민수", "지영"]
# print(names.index("민수")) # 2 출력

# 문제 5
# numbers = [10, 23, 36, 41, 50, 61, 72]
# for num in numbers:
#     if num % 2 == 0:
#         print(num)

# /////////////////////////
# 문제 1
# list1 = ["A", "B", "C"]
# list2 = ["D", "E", "F"]
# combi = list1 + list2
# print(combi)

# 문제 2
# numbers = [1,2,3]
# A_list = numbers*2
# print(A_list)

# 문제 3
# numbers = [4, 8, 15, 16, 23, 42]
# print(sum(numbers))

# 문제 4
# languages = ["Java", "C++", "Python", "JavaScript"]
# if "Python" in languages:
#     print("포함")
# else:
#     print("미포함")

# 문제 5
# numbers = [34, 12, 78, 56, 90, 21, 44]
# print(max(numbers))
# print(min(numbers))

# ////////////////////////////////////
# 문제 3 , 컴프리헨션션
# [표현식 for 변수 in 리스트 if 조건식]

# /////////////////////////////

# 문제 1
# numbers = [1,2,3,4,5,6]
# print(sum(numbers))

# total = 0 
# for num in numbers:
#     total += num
# print(total)

# 문제 2
# numbers = [1,2,3,4,5,6,7,8,9]
# for num in numbers:
#     if num % 2 == 0:
#         print(num)

# 문제 3
# numbers = [1,2,3,4,5,6,7,8,9]
# print(max(numbers))
# print(min(numbers))

# 문제 4
# fruits = ["사과", "바나나", "포도", "바나나", "딸기", "바나나"]
# for item in fruits:
#     result = [item for item in fruits if item != "바나나"]
# print(result)

# 문제 5 
# numbers = [12, 49, 67, 32, 80, 90, 25]
# count = 0
# for num in numbers:
#     if num > 50:
#         print(num)
#         count += 1
# print(count)

# ///////////////////////////
# 문제 1
# numbers = [[10, 20, 30], [40, 50, 60], [70, 80, 90]]
# print(numbers[2])

# 문제 2, 
# 배열일 때는 sort
# 원본만 수정할 때

# 뭐기기일 때는 sorted
# 원본을 가지고 추가적으로 수정을 거칠때?

# numbers = [10, 20, 10, 30, 20, 40, 50, 30]
# print(sorted(set(numbers)))

# 문제 3, 이날은 기억함함
# numbers = [1, 2, 3, 4, 5, 6]
# for item in numbers:
#     if item % 2 == 0:
#         print(item *2)
#     else:
#         print(item)


# result = [num*2 for num in numbers if num % 2 == 0]
# ab = [num1 for num1 in numbers if num1 % 2 == 1]
# print(sorted(result+ab))


# 문제 4
# def square_list(numbers):
#     return [ num **2 for num in numbers]

# numbers = [1,2,3,4,5]
# print(square_list(numbers))

# 문제 5
# numbers = [10, 20, 30, 40, 50]
# aver = sum(numbers) / len(numbers)
# print(aver)
# result = [num for num in numbers if num > aver]
# print(result)


# aver = ((10+20+30+40+50)/5)
# result = [num for num in numbers if num > aver]
# print(result)



