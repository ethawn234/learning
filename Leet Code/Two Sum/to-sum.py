class Solution:
    def twoSum(self, nums: list[int], target: int):
        """
        The goal is o(n) by finding the solution in a single list traversal.

        The idea is to add the current number and its index to a dict. If
        the complement of the current number exists in the dict, then we know
        that we have a solution.
        """
        d = {}
        
        for i, n in enumerate(nums):
            complement = target - n

            if complement in d:
                tc = [d[complement], i]
                print(tc)
                return tc
            else: 
                d[n] = i

toSum = Solution()
toSum.twoSum([3,2,4], 6)