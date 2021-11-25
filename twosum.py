class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        hash = {}
        for i in range(len(nums)):
            hash[nums[i]] = i
        print(hash)
        for i in range(len(nums)):
            complement = target - nums[i]
            if complement in hash and hash[complement] != i:
                return [i, hash[complement]]
        
        
        
        # for i in range(len(nums)):
        #     for j in range(i  + 1, len(nums)):
        #         if nums[j] + nums[i] == target:
        #             return i,j
         
