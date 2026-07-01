class Solution:
    def sortColors(self, nums: List[int]) -> None:
        #two pass approach
        # zero = 0
        # one = 0
        # two = 0

        # for i in range (len(nums)):
        #     if nums[i] == 0:
        #         zero += 1

        #     elif nums[i]==1:
        #         one += 1

        #     else: 
        #         two += 1

        # i = 0

        # while zero > 0:
        #     nums[i] = 0
        #     i += 1
        #     zero -= 1

        # while one > 0:
        #     nums[i] = 1
        #     i += 1
        #     one -= 1

        # while two > 0:
        #     nums[i] = 2
        #     i += 1
        #     two -= 1'

        #single pass approach

        left = 0
        mid = 0
        right = len(nums) - 1

        while mid <=right :
            
            if nums [mid] == 0:
                nums[left], nums[mid] = nums [mid], nums[left]
                left += 1
                mid +=1

            elif nums[mid] == 1:
                mid += 1

            else:
                nums[right], nums[mid] = nums [mid], nums[right]
                right -= 1
                

        


    




        


        