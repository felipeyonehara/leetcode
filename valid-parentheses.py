class Solution:

    def isValid(self, s) -> bool:
        stack = []
        closeToOpen = { ")" : "(", "]" : "[", "}" : "{" }


        for c in s: 
            if c in closeToOpen:
                print(f"{stack} and {stack[-1]}")

                if stack and stack[-1] == closeToOpen[c]:
                    stack.pop()
                else:
                    return False
            else:
                stack.append(c)

        return True if not stack else False

#valid code until here
string = "()"
s = Solution()

print(s.isValid(string))