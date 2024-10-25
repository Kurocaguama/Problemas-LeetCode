class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        if m == 0:
            nums1.clear()
            for i in nums2:
                nums1.append(i)
            return

        if n == 0:
            return

        lista_aux = nums1[0:m]

        a = 0
        b = 0
        lista_aux.append(6000000000)
        nums2.append(6000000000)
        print(lista_aux, nums2)
        for i in range(len(nums1)):
            print(f"iteración: {i}", "a, b:", a, b, "valores a comparar", lista_aux[a], nums2[b])
            print(lista_aux[a], nums2[b])
            if lista_aux[a] <= nums2[b]:
                nums1[i] = lista_aux[a]
                a+=1
            elif lista_aux[a] > nums2[b]:
                nums1[i] = nums2[b]
                b+=1
            print(nums1)