#rotate

Test = [4,5,6,7,8,9,10,12]

def solution(A, K):
    while K != 0:
        for x in range(len(A)):
            if(x == 0):
                temps = A[-1]
            temp = A[x]
            A[x] = temps
            temps = temp
        K -= 1
        print(A)

B = int(input("Rotate round :"))
print (len(Test))
solution(Test,B)

def solution(A):
    # write your code in Python 3.6
    A = sorted(A)
    for x in range(len(A)):
        temp = A[x]
        count=1
        for y in range(len(A)):
            if x == y:
                continue
            elif temp == A[y]:
                count += 1 
            else:
                result = temp
    return result