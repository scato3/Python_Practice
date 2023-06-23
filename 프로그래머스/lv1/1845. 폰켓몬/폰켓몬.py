def solution(nums):
    pocket = len(nums) / 2
    set_pocket = set(nums)
    answer = min(pocket, len(set_pocket))
    return answer