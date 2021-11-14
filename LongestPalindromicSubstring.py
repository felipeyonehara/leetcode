class Solution:
    def longestPalindrome(self, s: str) -> str:
        longest = 1
        temp = ""
        if(len(s) == 1): return s
        if(s == None): return ""
        
        
        def palindrome(string: str) -> bool:
            reverse = string[::-1]
            
            if reverse == string: return True
            else: return False
        
        
                
        for i in range(len(s)):
            # print(i, s[i:len(s)-i], s[i+1:len(s)-i], s[i:len(s)-i-1] )
            
            l = i
            r = len(s)
            # print(l, r)

            while(r > l):
                print(s[l:r])

                if(palindrome(s[l:r])):
                    # print(True)
                    temp = s[l:r]
                    if(longest < len(temp)):
                        longest = len(temp)
                        answer = temp
                        
                r=r-1
                print(s[l:r])
                if(palindrome(s[l:r])):
                    # print(True)
                    temp = s[l:r]
                    if(longest < len(temp)):
                        longest = len(temp)
                        answer = temp
        
        return answer