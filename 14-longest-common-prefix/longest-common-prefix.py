class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:

        prefix = ""

        for i in range(len(strs[0])):

            # Iterate through all the other words in strs
            for word in strs:
                
                # return prefix so far when characters do not match or length exceeded
                if i == len(word) or word[i] != strs[0][i]:
                    return prefix

            prefix += strs[0][i]

        return prefix



    

        
        