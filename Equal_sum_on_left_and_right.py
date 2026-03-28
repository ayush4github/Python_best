class Solution:
    def equilibrium(self, arr):
        total_sum = sum(arr)
        left_sum = 0
        for num in arr:
            total_sum = total_sum - num
            if left_sum == total_sum:
                return True
            left_sum = left_sum + num
            return False