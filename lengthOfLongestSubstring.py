class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        substring = set()

        a_pointer = 0
        b_pointer = 0
        max_size = 0
        
        while(b_pointer < len(s)):
            if(not s[b_pointer] in substring):
                substring.add(s[b_pointer])
                b_pointer += 1
                max_size = max(len(substring), max_size)
            else:
                substring.remove(s[a_pointer])
                a_pointer += 1

        return max_size