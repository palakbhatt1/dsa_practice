class Solution:
    def maxSubarraySum(self, arr, k):
        
        low = 0
        high = k-1
        total = 0
        
        for i in range (low, high +1):
                total += arr[i]
                
        res = total
                
        while high < len(arr)- 1:
            
            low +=1
            high +=1
            
            total = total - arr[low -1] + arr[high]
            
            res =  max(res, total)
        
        return res
            
        
