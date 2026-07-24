class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        hmap = {}
        for index, num in enumerate(numbers):
            diff = target - num
            if diff != num:
                if diff in hmap:
                    return [hmap[diff] + 1, index + 1]
            hmap[num] = index
        