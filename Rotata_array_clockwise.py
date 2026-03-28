class Solution:
    def rotateArr(self, arr, d):
        #Your code here
        n = len(arr)
        d = d % n
        for i in range(d):
            arr[:d] = reversed(arr[:d])
            arr[d:] = reversed(arr[d:])
            arr.reverse()
            return arr