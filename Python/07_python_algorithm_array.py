"""
덧셈하여 타겟을 만들 수 있는 배열의 두 숫자 인덱스를 리턴하라
입력 : nums = [2, 7, 11, 5], target = 9
출력 : [0, 1]
"""
# 투 포인터
def target_indexes(nums, target):
    nums.sort()
    left = 0
    right = len(nums)-1
    while left != right:
        if nums[left] + nums[right] < target:
            left += 1
        elif nums[left] + nums[right] > target:
            right -= 1
        else:
            return [left, right]

print(target_indexes(nums = [2, 7, 11, 15], target = 9))

'''
높이를 입력받아 비가 온 후 얼마나 많은 물이 쌓일지?
입력 : [0,1,0,2,1,0,1,3,2,1,2,1]
출력 : 6
'''

'''
배열을 입력받아 합으로 0을 만들 수 있는 3개의 엘리먼트를 출력
입력 : nums = [-1, 0, 1, 2, -1, -4]
출력 : [ [-1, 0, 1], [-1, -1, 2] ]
'''
def three_elem_with_brute(nums):
    answer = []
    nums.sort()
    for i in range(len(nums)-2):
        if i>0 and nums[i] == nums[i-1]:
            continue
        for j in range(i+1,len(nums)-1):
            for k in range(j+1,len(nums)):
                if nums[i] + nums[j] + nums[k] == 0:
                    answer.append([nums[i], nums[j], nums[k]])
    return answer
print(three_elem_with_brute(nums = [-1, 0, 1, 2, -1, -4]))

def three_elem_with_two_pointer(nums):
    answer = []
    nums.sort()
    for i in range(len(nums)-2):
        if i>0 and nums[i] == nums[i-1]:
            continue
        left, right = i+1, len(nums)-1
        while left < right:
            if nums[i] + nums[left] + nums[right] > 0:
                right -= 1
            elif nums[i] + nums[left] + nums[right] < 0:
                left += 1
            else:
                answer.append([nums[i], nums[left], nums[right]])
                while left < right and nums[left] == nums[left + 1]:
                    left += 1
                while left < right and nums[right] == nums[right - 1]:
                    right -= 1
                left += 1
                right -= 1
    return answer
print(three_elem_with_two_pointer(nums = [-1, 0, 1, 2, -1, -4]))


'''
n개의 페어를 이용한 min(a,b)의 합으로 만들 수 있는 가장 큰 수 출력
입력 : [1, 4, 3, 2]
출력 : 4
'''

'''
배열을 입력받아 output[i]가 자신을 제외한 나머지 모든 요소의 곱셈이 되도록 출력
입력 : [1, 2, 3, 4]
출력 : [24, 12, 8, 6]
단 나눗셈을 하지 않고 O(n)에 풀이하라
'''

'''
한 번의 거래로 낼 수 있는 최대 이익은?
입력 : [7, 1, 5, 3, 6, 4]
출력 : 5
'''
# 브루트 포스
def max_profit(prices):
    max_value = 0
    for i in range(len(prices) - 1):
        for j in range(i, len(prices)):
            value = prices[j] - prices[i]
            if max_value < value:
                max_value = value
    return max_value

print(max_profit(prices = [7,1,5,3,6,5]))
