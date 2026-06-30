class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        counter = {}
        n = len(nums)
        for i in range(n):
            counter[nums[i]] = counter.get(nums[i], 0) + 1
            if counter[nums[i]] > n/2:
                return nums[i]