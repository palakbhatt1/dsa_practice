class Solution:
    def segregate0and1(self, arr):
        i=0
        j=len(arr)-1
        
        while i<j:
            if arr[i]==0:
                i+=1
            
            elif arr[j]==1:
                j-=1
            
            else:
                arr[i],arr[j]=arr[j],arr[i]
                i+=1
                j-=1
        return arr
        
