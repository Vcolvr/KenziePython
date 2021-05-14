def solution(a, b):
    lengthA = len(a)
    lengthB = len(b)

    if lengthA > lengthB:
        return b + a + b
    
    else:
        return a + b + a
    