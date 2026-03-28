class Solution:
    def removeSpecialCharacter(self, s):
        result = []
        for char in s:
            if char.isalpha():
                result.append(char)
        if not result:
            return "-1"
        return ''.join(result)