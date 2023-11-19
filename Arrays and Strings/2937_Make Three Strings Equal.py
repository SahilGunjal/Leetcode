"""
You are given three strings s1, s2, and s3. You have to perform the following operation on these three strings
as many times as you want. In one operation you can choose one of these three strings such that its length is at
least 2 and delete the rightmost character of it.

Return the minimum number of operations you need to perform to make the three strings equal if there is
a way to make them equal, otherwise, return -1.

"""
# Complexity : O(len(common_string))

class Solution:
    def findMinimumOperations(self, s1: str, s2: str, s3: str) -> int:
        ptr1 = 0
        ptr2 = 0
        ptr3 = 0
        total_min_equal = 0
        while ptr1 < len(s1) and ptr2 < len(s2) and ptr3 < len(s3):
            if s1[ptr1] == s2[ptr2] and s2[ptr2] == s3[ptr3]:
                ptr1 += 1
                ptr2 += 1
                ptr3 += 1
                total_min_equal += 1
            else:
                break

        if total_min_equal == 0:
            return -1

        else:
            total_operations = 0
            total_operations += len(s1) - total_min_equal
            total_operations += len(s2) - total_min_equal
            total_operations += len(s3) - total_min_equal

            return total_operations

