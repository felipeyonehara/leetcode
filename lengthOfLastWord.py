class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        
        if(s==" "): return 0
        if(len(s) == 1 and s != " "): return 1
    
    
        for i in range(len(s)-1,-1,-1):
            print(i)
            if(s[i] == " "):                
                pointer = i
                word = 0
                if( pointer < len(s)-1 ):
                    # print("entrou")
                    return (len(s)-1-i)
                else:
                    # print("entrou 1")
                    # print(word)
                    # print(pointer)
                    while (s[pointer] == " " and pointer >= 0):
                        # print("entrou 2")                                                
                        pointer -=1
                    # print(word)
                    # print(pointer)
                    while (s[pointer] != " " and pointer >= 0):
                        # print("entrou 3")
                        word += 1
                        pointer -= 1
                    # print(word)
                    # print(pointer)
                    return word
            
        return len(s)