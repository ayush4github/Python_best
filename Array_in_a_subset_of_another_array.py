class Solution:
    def isSubset(self, a, b):
        if len(a) > len(b):
            return 'false'
        freq = {}
        for num in b:
            freq[num] = freq.get(num, 0)+1
        for num in a:
            if num not in freq or freq[num] == 0:
                return 'false'
            freq[num] = freq[num] - 1
        return 'true'