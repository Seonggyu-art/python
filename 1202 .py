# message = "Have a nice day"
# message = 0
# %d # 정수를 의미
# %f # 실수를 의미
# %s # 문자열을 의미

# print("오늘은 12월 %d일 입니다." % 2)
# print("오늘은 %d월 %d일 입니다." % (12,2))
# print("오늘은 %d%s %d일 입니다." % (12,'월',2))
# print(f"오늘은 {12}{'월'} {2}일 입니다.") ## 이게 깔끔함
# print("오늘은 " +str(12)+"월"+str(2)"일 입니다.")
# print("오늘은 ",12,"월",2,"일 입니다.",sep="") ## 이게 깔끔함.

# print("Hello".upper()) #대문자로 변환, 코딩테스트 단골 문제
# print("Hello".lower)() #소문자로 변환

# find() # 왼쪽부터 해당 문자 찾음
# rfind() # 오른쪽부터 해당 문자 찾음

# split() # 문자열을 공백이나 당른 문자로 나누어 리스트로 반환

# friends = "고찬국 김다운 김민창" #코딩테스트 단골 문제
# a = friends.split("김")
# print(a)

# sentence = "{}월 {}일".format(12,2)
# print(sentence)
# sentence = "{1}월 {0}일".format(12,2)
# print(sentence)
# sentence = "{0}월 {1}일".format(12,2)
# print(sentence)

# b = "   111  222    "
# print(b.strip())
# print(b.split())

# replace # 컨트롤 H?
# print(b.replace("111","333")) #뭔데 안나옴.

#실습 2
# num1 = int(input("첫번째 곱하고 싶은 세자리 자연수를 입력"))
# num2 = int(input("두번째 곱하고 싶은 세자리 자연수를 입력"))
# ones = num2 % 10
# tens = (num2 // 10) % 10
# hundreds = num2 // 100

# line1 = num1 * ones
# line2 = num1 * tens
# line3 = num1 * hundreds
# result = num1 * num2

# print(line1)
# print(line2)
# print(line3)
# print(result)

# #실습 더 빠르게 하는 방법
# a = input("세자리 넣어라")
# b = input("세자리 넣어라")

# print(int(a) * int(b[2]))
# print(int(a) * int(b[1]))
# print(int(a) * int(b[0]))
# print(int(a) * int(b))

# print(1==2)
# x = 2
# print(1<x<3)
# print(True and False)
# print(True or False)
# # print(not True)

# # cart = ["계란","콩나물","마늘","커피"]
# # print("두부" in cart)
# # print("계란" in cart)

# # if 1<3:
# #     print("True")
# #     print("True")
# # print("False")

# # #실습 3
# # a = int(input("숫자 입력하면 홀짝 구분해줌 "))
# # if a == (a // 2) * 2:
# #     print("짝")
# # if a != (a // 2) * 2:
# #     print("홀")

# # 실습 4
# # a = int(input("내 점수 등급 확인"))

# # if a >= 90:
# #     print("A")
# # elif a >= 80:
# #     print("B")
# # elif a >= 70:
# #     print("C")
# # elif a >= 60:
# #     print("D")
# # else:
# #     print("E")

# #실습 5
# a = int(input("나이를 숫자로 입력바람."))
# b = input("결제방법을 입력해.('카드' 또는 '현금')")

# if a < 8:
#     요금 = "무료"
# elif a < 14:
#     if b == "카드":
#         요금 = 450
#     else:
#         요금 = "에러"
# elif a < 20:
#     if b == "카드":
#         요금 = 720
#     elif b == "현금":
#         요금 = 1000
#     else:
#         요금 = "에러"
# elif a < 75:
#     if b == "카드":
#         요금 = 1200
#     elif b == "현금":
#         요금 = 1300
#     else:
#         요금 = "에러"
# else:
#     요금 = '무료'

# if 요금 == "에러":
#     print("결제 방법은 '카드' 또는 '현금'만 가능")
# else:
#     print(f"{a}세의 {b}요금은 {요금}원 입니다.")

