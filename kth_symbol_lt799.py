#leetcode 779(medium) -kth symbol in grammer

class Solution:
    def kthGrammer(self,n: int,k: int:)-> int:
        cur = 0
        #introduce two pointers
        left,right = 1,2**(n-1)
  
        #perform binary search
        for _ in range(n -1):
            mid = (left + right) //2
            if k<= mid :
                right = mid
            else:
                left = mid +1
                cur = 0 if cur else 1
        return cur
#time complexity - O(n) - time depends on the input size
#space complexity - 0(1) - no extra memmory needed
