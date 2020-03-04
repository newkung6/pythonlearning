def solution(A):
    A = sorted(A)
    check = 1
    for x in range(len(A)):
        if A[x] == check:
            check += 1
        else :
            continue
    return check

def solution(A):
    min_num = 99999
    for x in range(len(A)):
        if x == 0:
            first = 0
            second = 0
            for y in range(len(A)):
                if y == 0:
                    first = first + A[y]
                else:
                    second = second + A[y]
            result = abs(first-second)
        else:
            first = first + A[x]
            second = second - A[x]
            result = abs(first-second)       
        if min_num > result:
            min_num = result
    return min_num