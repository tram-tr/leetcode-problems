class Solution {
public:
    void nextPermutation(vector<int>& nums) {
        int n = nums.size();
        if(n == 1){
            return;
        }

        int i = nums.size() - 2;
        while (i >= 0 && nums[i + 1] <= nums[i])
            i--;
        
        if (i >= 0) {
            int j = nums.size() - 1;
            while (nums[j] <= nums[i])
                j--;
            
            // swap
            int temp = nums[i];
            nums[i] = nums[j];
            nums[j] = temp;
        }
        reverse(nums.begin() + i + 1, nums.end());
    }
};
