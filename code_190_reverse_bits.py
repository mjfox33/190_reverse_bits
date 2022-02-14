class Solution:
    def reverseBits(self, n: int) -> int:
        temp = '{:032b}'.format(n)
        temp2 = list()
        for c in temp:
            temp2.append(c)
        temp2.reverse()
        return(int("".join(temp2),2))