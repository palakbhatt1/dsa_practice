class Solution {
public:
    int removeDuplicates(vector<int>& nums) {
        int low=0;
        int high=1;
        int unique=1;
        int n=nums.size();

        while(high<n){
            if(nums[high]==nums[high-1]){
                high++;
                continue;
            }
            else{
                low++;
                nums[low]=nums[high];
                unique++;
                high++;
            }
        }

        return unique++;
    }
};