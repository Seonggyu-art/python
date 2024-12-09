# 문제 1, 코딩테스트 연습
# array의 각 element 중 divisor로 나누어 떨어지는 값을 오름차순으로 
# 정렬한 배열을 반환하는 함수, solution을 작성해주세요.
# divisor로 나누어 떨어지는 element가 하나도 없다면 배열에 -1을 담아 반환하세요.

# def solution(arr, divisor):
#     result = [x for x in arr if x % divisor == 0]

#     if result:
#         return sorted(result)
#     else:
#         return[-1]
    
# print(solution([5, 9, 7, 10], 5))
# print(solution([2, 36, 1, 3], 1))
# print(solution([3, 2, 6], 10))

# 꿀팁 : print(1 if 1<0 else 0) 

# 문제 2
# 정수 배열 numbers가 주어집니다.
# numbers에서 서로 다른 인덱스에 있는 두 개의 수를 뽑아 더해서 
# 만들 수 있는 모든 수를 배열에 오름차순으로 담아 return 하도록 
# solution 함수를 완성해주세요

# def solution(numbers):
#     result_set = set()
#     for i in range(len(numbers)):
#         for j in range(i + 1, len(numbers)):
#             sum_value = numbers[i] + numbers[j]
#             result_set.add(sum_value)
    
#     # 집합을 리스트로 변환 후 오름차순 정렬
#     result_list = sorted(result_set)
    
#     return result_list

# print(solution([2, 1, 3, 4, 1]))
# print(solution([5, 0, 2, 7]))

# 문제 3 (숙련자 문제)
# 정수 n을 기준으로 n과 가까운 수부터 정렬하려고 합니다.
#  이때 n으로부터의 거리가 같다면 더 큰 수를 앞에 오도록 배치합니다. 
# 정수가 담긴 배열 numlist와 정수 n이 주어질 때 numlist의 원소를 n으로부터 
# 가까운 순서대로 정렬한 배열을 return하도록 solution 함수를 완성해주세요.

# 올려준거 풀어보기

# 문제 4
# 양의 정수 x가 하샤드 수이려면 x의 자릿수의 합으로 x가 나누어져야 합니다. 
# 예를 들어 18의 자릿수 합은 1+8=9이고, 18은 9로 나누어 떨어지므로 18은 하샤드 수입니다. 
# 자연수 x를 입력받아 x가 하샤드 수인지 아닌지 검사하는 함수, solution을 완성해주세요.
def solution(x):
    digit_sum = sum(int(digit) for digit in str(x))
    return x % digit_sum == 0


# 문제 5

# 문제 6




# git add "1207 .py" "st .py" "1207st .py"






