class Solution:
    def removeVowels(self, s):
        vowels = set('aeiouAEIOU')
        result = []
        for char in s:
            if char not in vowels:
                result.append(char)
        return ''.join(result)