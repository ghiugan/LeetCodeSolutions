class Solution:
    def reverseWords(self, s: str) -> str:

        # Split the words on whitespace and add to list
        res = s.split()

        # Reverse the order
        res.reverse()

        # Join the string with space in between words
        return " ".join(res)




        