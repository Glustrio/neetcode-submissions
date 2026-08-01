class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        res = []
        nums.sort()

        for index, num in enumerate(nums):
            if index > 0 and num == nums[index - 1]:
                continue
            l, r = index + 1, len(nums) - 1
            if num > 0:
                break
            while l < r:
                left = nums[l]
                right = nums[r]
                sum = left + right + num
                if sum > 0:
                    r -= 1
                elif sum < 0:
                    l += 1
                else:
                    res.append([num, left, right])
                    l +=1
                    while nums[l] == nums[l - 1] and l < r:
                        l += 1
        return res