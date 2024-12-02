# 과제 2
# 자판기 프로그램, 값을 입력받아 출력하기
# list = ['게토레이','레쓰비','생수','이프로']

# print("")
# drink = input("마시고 싶은 음료는?")

# if drink in list:
#     print(f"{drink}드세요.")
# else:
#     print("{drink}가 없네요.")

# # 과제 3
# 자판기 프로그램 응용,

list = ['게토레이', '게토레이', '레쓰비', '레쓰비', '생수', '생수', '생수', '이프로']

print(f"남은 음료수 : {list}")
role = input("\n사용자 종류 선택해:\n1. 소비자\n2. 주인\n입력: ").strip() #\n 엔터잖아.

if role == "1": # 이게 소비자
    drink = input("\n마시고 싶은 음료를 선택해: ").strip()

    if drink in list: # 음료가 자판기에 있을 때
        list.remove(drink) #음료를 제거함.
        print(f"\n{drink}를 줄게요.")
    else: # 음료가 없음.
        print(f"\n{drink}")

elif role == "2": # 주인일 때
    test = input(f"\n작업을 선택해요:\n1. 추가\n2. 삭제\n입력: ").strip()

    if test == "1": # 음료가 추가
        new_drink = input("\n추가할 음료 이름대:")
        list.append(new_drink)
        print(f"\n{new_drink}가 추가되었습니다.")
    elif test == "2": #음료 삭제
        remove_drink = input("\n삭제할 음료 이름을 입력해: ")
        if remove_drink in list:
            list.remove(remove_drink)
            print(f"\n{remove_drink}가 삭제됨.")
        else:
            print(f"\n{remove_drink}가 목록에 없음.")
    else: #잘못된 작업선택
        print("\n잘못된 작업 선택입니다.")
else: #잘못된 테스트(역할)
    print("\n잘못된 입력입니다. 1또는 2를 선택해주세요.")
print(f"\n남은 음료수 : {list}")
