def find_average(nums):
    sum = 0
    total = len(nums)
    solution = 0
    
    for n in nums:
        sum = sum + n
    
    if total != 0:
        solution = sum / total
    
    return solution
        