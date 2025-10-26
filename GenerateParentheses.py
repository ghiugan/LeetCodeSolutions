class Solution:
    def generateParenthesis(self, n: int) -> List[str]:

        # Only add open parenthesis if open < n
        #only add a closing parenthesis if closed < open
        # valid IFF open == closed == n

        stack = []
        res = []

        def backtracking(openN, closeN):

            # base condition
            if openN == n == closeN:
                res.append("".join(stack))
                return

            # add open parenthesis
            if openN < n:
                stack.append('(')
                backtracking(openN + 1, closeN)
                stack.pop()
    
            # add closing parenthesis
            if closeN < openN:
                stack.append(')')
                backtracking(openN, closeN + 1)
                stack.pop()


        backtracking(0,0)

        return res



            
            
            

            

        
