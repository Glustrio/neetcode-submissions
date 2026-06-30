class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        window = set()
        # sliding window
        L = 0 # Left pointer

        for R in range(len(nums)): # right pointer
            if R - L > k: # If outside the window
                window.remove(nums[L]) # Remove the leftmost element to keep the window limit
                L += 1 # Increment L moving the window to the right by 1
            if nums[R] in window:
                return True
            window.add(nums[R])
        return False

