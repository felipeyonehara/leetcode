class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        
        array = list()
        
        for i in range(len(nums)):
            
            try:
                # print(i)
                index = array.index(nums[i])
                # print("index:",index)
                # if(array is not None):
                array.pop(index)
            except ValueError:
                # print("add item", nums[i])
                array.append(nums[i])
                # print("array updated:",array)
                
        # print(array)
        return array.pop()
