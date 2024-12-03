class Solution:
    def fib(self, n: int) -> int:
        if n == 0:
            return 0
        if n == 1:
            return 1
        return self.fib(n-1) + self.fib(n-2)

    def tribonacci(self, n: int) -> int:
        # initial solution expanding the fibonacci code
        # does not get accepted by leetcode due to timeout restrictions

        #if n == 0 or n == 1:
        #    return n
        #if n == 2:
        #    return 1
        #return self.tribonacci(n-1) + self.tribonacci(n-2) + self.tribonacci(n-3)

        #second attempt using list hint

        a = [0 for i in range(40)] # 40 as a upper limit of n given by the problem
        a[0] = 0
        a[1] = 1
        a[2] = 1

        for i in range(3, n+1):
            a[i] = a[i-1] + a[i-2] + a[i-3]

        return a[n]
