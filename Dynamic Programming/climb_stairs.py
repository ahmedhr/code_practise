# Recursion

class Solution:
    def climbStairs(self, n: int) -> None:
        steps = 0
        return self.recur_climb(n, steps)

    def recur_climb(self, n, steps):
        if steps > n:
            return 0
        elif steps == n:
            return 1
        else:
            return self.recur_climb(n, steps + 1) + self.recur_climb(n, steps + 2)


n = 3

print(Solution().climbStairs(n))


# Memo + Recursion ---- Top - Bottom

class Solution:
    memo = {}

    def climbStairs(self, n: int) -> None:
        steps = 0
        return self.recur_climb(n, steps)

    def recur_climb(self, n, steps):
        if self.memo.get(steps):
            return self.memo[steps]
        if steps > n:
            return 0
        elif steps == n:
            return 1
        else:
            self.memo[steps] = self.recur_climb(n, steps + 1) + self.recur_climb(n, steps + 2)
            return self.memo[steps]


n = 4

print(Solution().climbStairs(n))


# Memo ---- Bottom - Top

class Solution:

    def climbStairs(self, n: int) -> int:
        memo = dict(int)
        memo[n - 1] = 1
        memo[n - 2] = 2
        n -= 3
        while not n < 0:
            memo[n] = memo[n + 1] + memo[n + 2]
            n -= 1
        return memo[0]


n = 4

print(Solution().climbStairs(n))