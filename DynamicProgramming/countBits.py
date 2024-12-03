class Solution:
    def countBits(self, n: int) -> List[int]:
        # Base cases n == 0 or n == 1
        if n == 0:
            return [0]

        if n == 1:
            return [0,1]

        # Verifying ammount of 1s in binary
        a = bin(n)[2:]
        valor_bin = 0
        for char in str(a):
            if char == '1':
                valor_bin+=1

        #Recursive argument, only accessible when n > 1
        aux = self.countBits(n-1)
        aux.append(valor_bin)

        return aux