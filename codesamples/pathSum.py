# Definition for a binary tree node.


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def hasPathSum(self, root: TreeNode, targetSum: int) -> bool:
    
        def PrintTree(self, value):
            if self.left:
                PrintTree(self.left, self.val + value)                
            print( self.val, value)
            if self.right:
                PrintTree(self.right, self.val + value)

        PrintTree(root,0)
        
        
        
        #isLeaf()
        #check if left and right are None and return 
        def isLeaf(self) -> bool:
            if(self.left and self.right):
                print("Leaf detected!")
                return True
            return False

input = "[5,4,8,11,None,13,4,7,2,None,None,None,1]"
solution = Solution()
solution.hasPathSum(input,22)