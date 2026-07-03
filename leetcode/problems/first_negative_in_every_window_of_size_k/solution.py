def firstNegInt(arr, k):
    res = []
    n = len(arr)
    
    for i in range(n - k + 1):
        found = False
        
        for j in range(k):
            
            if arr[i + j] < 0:
                res.append(arr[i + j])
                found = True
                break
       
        if not found:
            res.append(0)
    return res