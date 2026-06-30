class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        digits = digits[::-1]
        one, i = 1, 0
        while one:
            # if the digit is 9
            if i < len(digits):
                if digits[i] == 9:
                    digits[i] = 0
                else:
                    digits[i] += 1
                    one = 0 # ends loop
            # handles the case if all digits are 9
            else:
                digits.append(1)
                one = 0
            i += 1
        return digits[::-1]