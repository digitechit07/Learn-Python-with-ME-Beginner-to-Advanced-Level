
# Given four positive integers A, B, C, D, determine if there’s a rectangle such that the lengths of its sides are A, B, C and D (in any order).
# If any such rectangle exist return 1 else return 0.



class Solution:
    # @param A : integer
    # @param B : integer
    # @param C : integer
    # @param D : integer
    # @return an integer
    def solve(self, A, B, C, D):
        E=[A,B,C,D]
        E.sort()
        # print(E)
        if(E[0]==E[1] and E[2]==E[3]):
            return(1)
        else:
            return(0)
