class Solution:
    def findMin(self, nums: List[int]) -> int:
        low, high = 0, len(nums) - 1
        ans = nums[0]
    
        while low <= high:
            mid = (low + high) // 2  # Use integer division

        # If the current subarray is sorted
            if nums[low] <= nums[mid]:
                ans = min(ans, nums[low])
                low = mid + 1
            else:
                ans = min(ans, nums[mid])
                high = mid - 1

        return ans