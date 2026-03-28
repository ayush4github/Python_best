class Solutions:
    def minAnd2ndMin(self, arr):
        if len(arr) < 2:
            return [-1]
        smallest = float('inf')
        second_smallest = float('inf')
        for element in arr:
            if element < smallest:
                second_smallest = smallest
                smallest = element
            elif smallest < element < second_smallest:
                second_smallest = element
        if second_smallest == float('inf'):
            return [-1]
        return [smallest, second_smallest]