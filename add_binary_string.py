"""
https://leetcode.com/problems/add-binary/description/
Given Binary string str1 and str2, add them and return the sum as a binary string
Input2:
str1=100
str2= 010 (contains leading zero, use zfill to pad it with o's)
"""
class Solution:
    def addBinary(self, a: str, b: str) -> str:
        res = []
        carry = 0
        max_len = max(len(a), len(b))
        a = a.zfill(max_len)
        b = b.zfill(max_len)

        for i in range(max_len - 1, -1, -1):
            bit1 = int(a[i])
            bit2 = int(b[i])

            total = bit1 + bit2 + carry

            res_bit = total % 2
            res.append(str(res_bit))

            carry = total // 2

        if carry:
            res.append(str(carry))

        return ''.join(res[::-1])

