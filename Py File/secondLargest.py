'''You are given an integer array A. 
Return the second largest element. 
If no such element exist then return -1.'''

class Solution:
    # @param A : list of integers
    # @return an integer
    def solve(self, A):
        second_largest = 0 
        largest_val = 0 
        ele=A[0]
        chk=True
#to find largest elements
        for i in A:
            if(largest_val<i):
                largest_val=i

#to check if all the elements of list are not same
        for i in A:
            if ele != i:
                chk=False
                break
        if(chk==True):
            return(-1)
  
#to find second largest element
        for i in A:
            if(second_largest<i and i !=largest_val):
                second_largest=i
                
#to check if length of array is not less or equal to 2
        if(len(A) >=2 and second_largest !=0):
            return second_largest
            
        else:
            return -1
        
