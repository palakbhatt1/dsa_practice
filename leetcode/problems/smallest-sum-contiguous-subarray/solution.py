class Solution:
    def smallestSumSubarray(self, A, N):
        #Your code here
        b_e=A[0]
        ans = A[0]
        
        for i in range(1,N):
            
            v1 = b_e + A[i]
            v2 =  A[i]
            b_e =  min(v1, v2)
            ans = min(b_e,ans)
            
        return ans
