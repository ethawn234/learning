# total sum on each iteration:
{
    0: -2, 
    1: -1, 
    2: -4, 
    3: 0, 
    4: -1, 
    5: 1, 
    6: 2, 
    7: -3, 
    8: 1
}

# [-2,1,-3,4,-1,2,1,-5,4]

class Solution:
    @staticmethod
    def maxSubArray(nums: list[int]) -> int:
        historical_sum = nums[0]
        current_sum = nums[0]

        for i in range(1, len(nums)):
            if current_sum + nums[i] > nums[i]:
                current_sum += nums[i]
            else:
                current_sum = nums[i]

            if historical_sum < current_sum:
                historical_sum = current_sum

        print('The max sub-array in the given list is:\n', historical_sum)






















    
    def max_subarray(self, nums):
        """Find the largest sum of any contiguous subarray."""
        max_sum = nums[0]
        current_sum = nums[0]

        for n in nums:
            current_sum = max(n, current_sum + n)
            max_sum = max(max_sum, current_sum)
        print('max_subarray ',max_sum)

s = Solution()
s.maxSubArray([-2,1,-3,4,-1,2,1,-5,4])
s.max_subarray([-2,1,-3,4,-1,2,1,-5,4])