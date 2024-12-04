class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        if s == "":
            return True
        index_sub = 0
        aux = s[index_sub]
        for i in range(len(t)):
            if t[i] == aux:
                print(aux)
                index_sub += 1
                if index_sub < len(s):
                    aux = s[index_sub]
        
        if index_sub == len(s):
            return True
        else:
            return False