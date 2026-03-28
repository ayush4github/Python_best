class Solution:
    def removeChars(ob, str1, str2):
        remove_set = set(str2)
        result = []
        for char in str1:
            if char not in remove_set:
                result.append(char)
        return ''.join(result)