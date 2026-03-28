class Solution:
    def modify(self, s):
        result = []
        for char in s:
            if char != ' ':
                result.append(char)
        return ''.join(result)