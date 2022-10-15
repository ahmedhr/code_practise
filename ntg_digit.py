# class Solution:
#
#     def get_d(self, n):
#         a = 0
#         nin = mulfact = 9
#         i = 2
#         d = 0
#         mulpli = 10
#         while (True):
#             if n <= mulfact:
#                 return a, d
#             else:
#                 d = (d * 10) + 10
#                 a = mulfact
#                 mulfact = nin * i * mulpli
#                 mulpli *= 10
#                 i += 1
#
#     def findNthDigit(self, n: int) -> int:
#         if n < 10:
#             return n
#         num = 10
#         n = n - 10
#         d, num = self.get_d(n)
#         print(n, d, num)
#         while (True):
#             c = num
#             arr = []
#             while (True):
#                 mod = int(c % 10)
#                 arr.append(mod)
#                 c = int(c / 10)
#                 d += 1
#                 if c == 0:
#                     break
#             if n <= d:
#                 d -= len(arr) - 1
#                 for i in range(len(arr)):
#                     if n == d:
#                         return arr.pop()
#                     arr.pop()
#                     d += 1
#             num += 1


class Solution(object):
    def findNthDigit(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n <= 9: return n
        i, p = 1, 9
        while True:
            n += p
            p = p * 10 + 9
            i += 1
            if n < p * i:
                x = (n + i - 1)
                y = int(x // i)
                z = x % i
                return int(str(z))



print(Solution().findNthDigit(11))
