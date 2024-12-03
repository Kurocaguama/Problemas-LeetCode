class Solution:
    def climbStairs(self, n: int) -> int:
        #if n == 1:
        #    return 1
        #if n == 2:
        #    return 2
        #return self.climbStairs(n-1) + self.climbStairs(n-2) 
        
        #Esto es n^2, tenemos que bajar la complejidad, haremos el mismo truco de tribonacci

        a = [0 for i in range(46)]
        a[0] = 1
        a[1] = 2

        for i in range(2, 46):
            a[i] = a[i-1] + a[i-2]
        return a[n-1]