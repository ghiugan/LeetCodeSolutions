class Solution:
    def minOperations(self, s: str) -> int:

        # Count number of changes to match pattern A: 010101...
        # The number of changes for the other pattern is the inverse of the other
        # Return the min of countA and len(s) - countA

        count = 0

        for i in range(len(s)):

            # If it is an even index and '1' change 
            if i % 2 == 0 and s[i] == "1":
                count += 1

            # If it is an odd index and '0' change 
            elif i % 2 != 0 and s[i] == '0':
                count += 1

        return min(count, len(s) - count)


        