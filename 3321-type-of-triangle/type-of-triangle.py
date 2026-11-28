class Solution:
    def triangleType(self, nums: List[int]) -> str:
        # Sort the sides so we only need to check the two smallest against the largest
        nums.sort()
        
        # Check the triangle inequality theorem
        if nums[0] + nums[1] <= nums[2]:
            return "none"
        
        mySet = set(nums)
        if len(mySet) == 1:
            return "equilateral"
        if len(mySet) == 2:
            return "isosceles"
        return "scalene"
