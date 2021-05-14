def find_smallest_int(arr):
    solution = arr[0]
    for n in arr:
        if n < solution:
            solution = n
            
    return solution