class Solution {
public:
    vector<int> twoSum(vector<int>& arrs, int target) {
        int i = 0;
        int j =arrs.size() - 1;

        while(i<j){
            int sum =arrs[i]+arrs[j];

            if(sum == target){
                return {i + 1, j+1};
            }
            else if(sum<target){ 
                i++;
            }
            else {
                j--;
            }        
        }

        return{};

    }
};