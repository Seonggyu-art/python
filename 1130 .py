#print(2 + 4)
#print(1+2*-3**2)

#print("빵의 개수 :", 30//4)
#print("남은 빵의 개수 :", 30%4)

# a = 1
# a += 1 
# print(a)

# print("장원영"+"럭키")
# print("럭키"*10)

# song = input("너의 최애 노래는?")
# print(song)
# print(type(song))

# a = input("1+1=?")
# #print(a)
# print(int(a)*2)

# ff = float(input())

# a = 2
# print(str(2)*10)
# #print(str(2)+"입니다.")
# print(2+"입니다") # 에러

# print("|\\_/|")
# print("|q p|   /}")
# print("( 0 )\"\"\"\\")
# print("|\"^\"`    |")
# print("||_/=\\\\__|")

# print("|\_/|")
# print("|q p|  /}")
# print('(0) """\\')
# print('|"^"`   |')
# # print("||_=\\\__|")

# name = input("이름을 입력하세요: ")
# age = int(input("나이를 입력하세요.: "))

# print(f"안녕하세요! {name}님 ({age})세")

# name = input("이름을 입력하세요: ")
# birth_year = int(input("태어난 년도를 입력하세요.: "))
# current_year = int(input("올해 년도를 입력하세요.: "))

# age = current_year - birth_year
# next_year = current_year + 1

# print("올해는 " + str(current_year) + "년," + name + "님의 나이는 " + str(age) + "세 입니다.")

# name = input("이름을 입력해라.: ")
# print(name)

# mame = input("이름 대라. :")
# print(mame)

# a = []
# b = [0,1,2,3]
# c = ["장원영", "안유진"]
# d = [0, "아이브"]

# print(len(c))
# print(c[1])
# print(c[1])
# c[0] = "카리나"
# print(c)

# del c[0]
  
# print(b[-2])

# seasons = ["봄", "여름", "가을", "겨울"]
# # print(seasons[0:1])
# # print(seasons[0:2])
# # print(seasons[:2])
# # print(seasons[1:])
# # print(seasons[2:])
# # print(seasons[1:3])

# # print(seasons[:])
# # print(seasons)
# # print(seasons[::2])
# # print(seasons[::3])

# # print(seasons[::-1])

# seasons2 = ["반팔", "청바지", "이어폰", ["무선 키보드", "유선 키보드", "기계식 키보드"]]
# print(seasons2[-1][0])

# a = [1, 2, 3]
# b = [4, 5]
# print(a + b)
# print(a * 2)
# print(len(a))
# print(len(b))

# a = ["1","2","3","4","5","6","7","8","9","10"]
# print(a[1:11:2]) # 짝수 만들기
# print(a[1::2]) # 짝수 만들기

# print(a[0::2]) # 홀수 만들기
# print(a[0:11:2]) # 홀수 만들기

# a = [3,4,2,1]
# a.sort()
# print(a)

# b = ["a", "b", "c", "d"]
# b.sort()
# print(b)

# c = ["1", "10", "11", "2"]
# c.sort()
# print(c)

# d = ["강남", "강북", "서"]
# d.sort()
# print(d)

# a = [3,4,2,1]
# a.reverse()
# print(a)

# shop = ["a", "b", "c", "d"] 
# shop.append("e") #맨 뒤에 추가
# shop.remove("b") #삭제
# print(shop)

# shop.inset() # 특정 위치에서 추가
# shop.pop(1)
# del shop

# print(d. index("서")) #위치찾기

# d = ["강남", "강북", "서", "서", "서"] #앙 몰라
# first = d.index("서")+1
# print(first + d[first+1:].index("서"))
# d. count("서") #숫자세기 단, 1개 이상일때 가능

rainbow = ['red', 'orange', 'yellow', 'green', 'blue', 'indigo', 'purple']
print(rainbow[2]) #2번 인덱스 값 출력
rainbow.sort() 
print(rainbow[0:6]) #알파벡 순서로 정렬한 값 출력
rainbow.append('black') 
print(rainbow) # 좋아하는 색 맨 마지막에 추가
del rainbow[3:-1]
print(rainbow) # 3-6번째 값 삭제하기
