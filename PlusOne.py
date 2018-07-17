"""
Given a non-empty array of digits representing a non-negative integer, plus one to the integer.

The digits are stored such that the most significant digit is at the head of the list, and each element in the array contain a single digit.

You may assume the integer does not contain any leading zero, except the number 0 itself.

Example 1:

Input: [1,2,3]
Output: [1,2,4]
Explanation: The array represents the integer 123.
Example 2:

Input: [4,3,2,1]
Output: [4,3,2,2]
Explanation: The array represents the integer 4321.
"""


class Solution:
    def plusOne(self, digits):
        """
        :type digits: List[int]
        :rtype: List[int]
        """
        n = len(digits)
        if digits[n - 1] < 9:
            digits[n - 1] = digits[n - 1] + 1
            return digits
        i = n - 1
        result = []
        carry = 1
        while n:
            if digits[i] == 9 and carry:
                result.append(0)
                carry = 1
            elif carry:
                result.append(digits[i] + 1)
                carry = 0
            else:
                result.append(digits[i])

            i -= 1
            n -= 1
        if carry:
            result.append(1)
        return result[::-1]

l = [2,4,9,3,9]
x = Solution().plusOne(l)
print(x)