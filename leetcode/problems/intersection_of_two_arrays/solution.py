class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        
        freq1 = {}
        freq2 = {}
        result = []

        for i in range(len(nums1)):
            freq1[nums1[i]] = freq1.get(nums1[i],0)+ 1

        for i in range(len(nums2)):
            freq2[nums2[i]] = freq2.get(nums2[i],0)+ 1

        for num in freq1:
            if num in freq2:
                result.append(num)

        return result



    

