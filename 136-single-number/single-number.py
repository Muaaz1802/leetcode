class Solution:
    def singleNumber(self, nums):
        result = 0

        for num in nums:
            result ^= num  # XOR cancels duplicates

        return result