class KeyPair:
    def isValid(self, key) -> bool:
        stack = []
        alphabet = { "a" : "1",
                     "b" : "2", 
                     "c" : "3", 
                     "d" : "4", 
                     "e" : "5", 
                     "f" : "6", 
                     "g" : "7", 
                     "h" : "8", 
                     "i" : "9", 
                     "j" : "10", 
                     "k" : "11"}
        for letter in key:
            if letter in alphabet:
                print("letter in alphabet")
                print(f"{stack} and {stack[-1]} and {alphabet[letter]}")
                if stack and stack[-1] == alphabet[letter]:
                    stack.pop()
                else: return False
            else:
                print("letter NOT in alphabet")
                stack.append(letter)
        return True if not stack else False

string = "1a2b3c"
s = KeyPair()

print(s.isValid(string))