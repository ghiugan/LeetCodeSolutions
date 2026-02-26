class Solution:
    def jump(self, nums: List[int]) -> int:

        jump = 0 # This will be the min # of jumps
        l = r = 0 # the index window
        
        while r < len(nums) - 1:
            farthest = 0 # farthest value we can jump

            # Check possible jumps in context window
            for i in range(l, r + 1):

                farthest = max(farthest, i + nums[i])

            l = r + 1
            r = farthest
            jump += 1

        return jump





        


        