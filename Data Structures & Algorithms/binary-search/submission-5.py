class Solution:
    def search(self, nums: List[int], target: int) -> int:
        mid = len(nums)//2
        l = 0
        r = len(nums)-1

        go = True
        while go:
            if target == nums[mid]:
                return mid
            elif l == mid and r == mid:
                return -1
            elif target < nums[mid]:
                r = mid -1
                if r < 0:
                    return -1

            elif target > nums[mid]:
                l = mid + 1
                if r > len(nums)-1:
                    return -1

            mid = (l+r)//2
            

        return -1

