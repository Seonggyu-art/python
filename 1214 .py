# 데이터 분석
# 실습. Numpy 모듈 사용해보기 1
# 10개의 0으로 채워진 array를 만들고 출력
# 1번에서 만들어진 array에서 5번째 값을 1로 바꾸고 출력
# 10부터 30까지의 수로 이루어진 array를 만들고 출력
# 0부터 99까지의 난수로 이루어진 2x2 arrary를 만들고 출력
# 0부터 1사이의 난수로 이루어진 2x4 arry를 만들고 출력

# import numpy as np

# array = np.zeros(10)
# print("1번 문제:", array)

# array[4] = 1
# print("2번 문제:", array)

# array2 = np.arange(10, 31)
# print("3번 문제:", array2)

# array3 = np.random.randint(100, size=(2, 2))
# print("4번 문제:", array3)

# array4 = np.random.rand(2, 4)
# print("5번 문제:", array4)

# 실습. Numpy 모듈 사용해보기2
# 35부터 74까지의 순차적인 수로 이루어진 1차원 배열을 만들고 10X4 행렬로 변환 후 출력
# 6부터 만든 배열을 맨 끝의 행부터 역순으로 출력
# 6에서 만든 배열 중 두 번째 행부터 마지막 직전 행까지, 세번째 열부터 마지막 열까지 슬라이싱해서 출력
# 6에서 만든 배열에서 마지막 열에 해당하는 모든 값을 출력(1차원 배열로)
#  #6에서 만든 배열에서 마지막 열에 해당하는 모든 값을 출력(2차원 배열로)
# 9-1에서 만든 배열로 역순으로 정렬해서 출력
# 1부터 50까지의 난수로 된 5x6 배열을 만들고, 배열에서 짝수만 선택하여 출력하는 코드를 작성

# import numpy as np

# array_6 = np.arange(35, 75).reshape(10,4)
# print("\n6번 문제\n", array_6)

# reversed_rows = array_6[::-1]  # 행 순서를 역순으로 뒤집음
# print("\n7번 문제\n:", reversed_rows)

# sliced_array = array_6[1:-1, 2:]
# print("\n8번 문제\n", sliced_array)

# nine_num = array_6[:, -1]
# print("\n9번 문제\n", nine_num)

# nine_one = array_6[0:,-1:]
# print("\n 9-1 문제\n", nine_one)

# a10 = array_6[::-1, -1:]
# print("\n10번\n", a10)

# a11 = np.random.randint(1,51,size=(5,6))
# print(a11)
# even11 = (a11 % 2 == 0)
# even_num = a11[(even11)]
# print(even_num)


# 데이터 분석 numpy 2 , 쓰는 파일 다름.

# import numpy as np
# a = np.array([1,2],[3,4])

# expanded = np.expand_dims(a,2)
# print(expanded)
# print(expanded.shape)

# # 차원 축소 
# np_ones = np.ones((1,2,1,3))
# print(np_ones)

# sq = np.squeeze(np_ones)
# print(sq)
# print(sq.shape)

# 중복 제거
# 중복된 요소 제거

import numpy as np

a = [1,2,2,3,4,3,4,3,1]
u_a, counts = np.unique(a, return_counts = True)
print(u_a)
print(counts)

a = [1,2,2,3,4,3,4,3,1]
u_a, indexs = np.unique(a, retuern_index=True)
print(u_a)
print(indexs)

a = [1,2,2,3,4,3,4,3,1]
u_a, indexs, counts = np.unique(a, retuern_index=True, return_counts=True)
print(u_a)
print(indexs)
print(counts)

a = [1,2,2,3,4,3,4,3,1]
u_a, indexs, indexs = np.unique(a, retuern_index=True, return_counts=True)
print(u_a)
print(indexs)
print(counts)

# 1214.inpynb로 넘어갔어야 했는데, 일단 여기까지 py로 함.
