class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        def iteration(ll):
            l_norm = []
            while (ll != None):
                l_norm.append(ll.val)
                ll = ll.next
            return l_norm

        def cum_sum(l_norm):
            aux = 0
            for i in range(len(l_norm)):
                aux += (10**i) * l_norm[i]
            return aux
        
        def getting_list(a, b):
            a_norm = iteration(a)
            b_norm = iteration(b)

            a_sum = cum_sum(a_norm)
            b_sum = cum_sum(b_norm)

            c = str(a_sum + b_sum)
            c_list = [int(i) for i in c]
            return c_list[::-1]

        sum_list = getting_list(l1, l2)
        
        ret = ListNode()
        ret1 = ret
        for _ in sum_list:
            aux = ListNode(_)
            ret1.next = aux
            ret1 = ret1.next
        res = ret.next
        ret.next = None
        return res