class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """

        k %= len(nums)

        def reverse(l, r):
            while l < r:
                nums[l], nums[r] = nums[r], nums[l]
                l += 1
                r -= 1


        # First reverse entire list once
        reverse(0, len(nums) - 1)

        # Reverse first k elements
        reverse(0, k - 1)

        # Reverse remaining elements of list
        reverse(k, len(nums) - 1)
