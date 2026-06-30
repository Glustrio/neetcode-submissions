class Solution:
    def isValid(self, s: str) -> bool:
        hashmap = { "]": "[", ")": "(", "}" : "{"} # maps close parentheses to open parentheses
        stack =[]
        # brackets/parentheses are interchangeable for comments

        for bracket in s: # for each brack in s
            if bracket in hashmap: # if bracket is a key of hashmap (meaning it's a key of hashmap, the dict)
                if stack and stack[-1] == hashmap[bracket]: # if stack is nonempty and top of stack is equal to the opening parentheses of the closing parentheses
                    stack.pop()
                else: # Else the closing bracket doesn't match the respective opening bracket
                    return False
            else: # If it's an opening bracket
                # Add (or push in stack terms) the bracket to the stack so that we can check if the first element in stack (which contains all the opening brackets) matches the closing brackets in the hashmap
                stack.append(bracket)
            
        return True if not stack else False


        