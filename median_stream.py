class MedianFinder:

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.data_stream = []

    def addNum(self, num: int) -> None:
        if self.data_stream:
            n = len(self.data_stream)
            l = 0
            h = n - 1
            m = int(n // 2)
            while True:
                if num == self.data_stream[m]:
                    self.data_stream.insert(m, num)
                    return
                if num < self.data_stream[m]:
                    if l == m:
                        self.data_stream.insert(l, num)
                        return
                    else:
                        h = m - 1
                        m = (h + l) // 2
                elif num > self.data_stream[m]:
                    if h == m:
                        self.data_stream.insert(h + 1, num)
                        return
                    else:
                        l = m + 1
                        m = (h + l) // 2

        self.data_stream.append(num)

    def findMedian(self) -> float:
        n = len(self.data_stream)
        if n == 1:
            return self.data_stream[0]
        if n % 2:
            return self.data_stream[int(n / 2)]
        return (self.data_stream[int((n - 1) / 2) + 1] + self.data_stream[int((n - 1) / 2)]) / 2


"""
https://leetcode.com/problems/find-median-from-data-stream/
["MedianFinder","addNum","addNum","findMedian","addNum","findMedian"]
[[],[1],[2],[],[3],[]]
"""
