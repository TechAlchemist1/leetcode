class Solution:
    def minOperations(self, nums: list[int], x: int) -> int:
        '''
        Max num of operations to zero: Remove from the left most or 
        right most element in the array, each element we remove subtracts
        the sum from x:

        We want to keep the longest possible middle section(which will hold the minimum operations inveriant)

        We can keep a prefix sum + map -> The question we need answered at each point is 

        at each prefix we ask can we subtract a value from our left such that such that the sum
        of the new subarray is equal to sum(nums) - x. 

        Two conditions either it happens or doesnt:
        donest case is simple: We continue
        does   case we calculate the differences in index where we calculate the amount of operations 

        '''
        # Contains the total current sum and start index for this sum
        myMap = {0:-1}
        prefix = 0
        total = sum(nums)
        ans = -1

        for i in range(len(nums)):
            prefix += nums[i]
            # determin if we can subtract a subarray such that: totalPrefix - prefix = sum(nums) - x
            # totalPrefix - (sum(nums) + x) : look for this in the map
            valid = prefix - total + x
            if valid in myMap:
                # calculate the size of the middle array after subtracting 
                size = i - myMap[valid]
                # ensure we keep track of longest so we keep the minimal changes
                ans = max(ans,size)
            # this is after where we add to our map
            myMap[prefix] = i
        # one more special condition maybe removing the entire arr works
        if total - x == 0:
            return len(nums)
        # ans represents the size of the valid arr so len(arr) - longest is what we want
        if ans == -1:
            return -1
        return len(nums) - ans