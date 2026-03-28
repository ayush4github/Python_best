class Solution:
    def maxCoins(self, A, B, T, N):
        boxes = list(zip(B, A))
        boxes.sort(reverse=True)
        total = 0
        for coins, plates in boxes:
            if T == 0:
                break
            take = min(plates, T)
            total += take * coins
            T -= take
            return total