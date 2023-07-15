def maximum_sum_subarray(A, B, C):
    start=0
    end=0
    currentSum=C[0]
    maxSum=0
    while end<A:
        if currentSum<=B:
            maxSum=max(maxSum, currentSum)
            if maxSum==B:
                return B
            end+=1
            if end<A:
                currentSum+=C[end]
        else:
            currentSum-=C[start]
            start+=1
    return maxSum
A=int(input("Enter the size of the array:"))
B=int(input("enter the maximum sum:"))
C=list(map(int, input().split()))
print(maximum_sum_subarray(A,B,C))
