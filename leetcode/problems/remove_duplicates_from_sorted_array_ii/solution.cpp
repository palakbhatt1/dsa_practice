class Solution {
public:
    int removeDuplicates(vector<int>& nums) {
        int low = 1;
        int high = 2;
        int n = nums.size();

        if(n<=2) return n;

        while(high<n){
            if (nums[high]==nums[low-1]){
                high++;
                continue;
            }
            else{
                low++;
                nums[low]=nums[high];
                high++;
            }
        }
        return low+1;

        
    }
};