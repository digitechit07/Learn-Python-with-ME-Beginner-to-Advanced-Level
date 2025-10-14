# Given an array A of size N, pick 2 indices i and j such that
# 1 <= i, j <= N
# A[i] % A[j] is maximum among all possible pairs of (i, j).
# Find the maximum value of A[i] % A[j] for some i, j.

class Solution:
    # @param A : list of integers
    # @return an integer
    def solve(self, A):
        N=len(A) 
        first=-sys.maxsize-1      # sys.maxsize-1 gives the smallest possible value for an integer
        second=-sys.maxsize-1
        i=0
        for i in range(N-1):
            if(A[i]>first):
                second=first
                first=A[i]
            
            elif(A[i]>second and A[i]!=first):
                second=A[i]
        #to check if all elements are same or not
        checkSimilar = all(element == A[0] for element in A) 
        if (checkSimilar):
            return 0
        else:
            return second
            


