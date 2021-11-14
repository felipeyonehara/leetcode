class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        k = 0
        current_pointer = 0
        
        for i in range(len(nums)):
            if (nums[i] != nums[current_pointer]):
                current_pointer += 1
                nums[current_pointer] = nums[i]
                k += 1
        
        
        return k+1