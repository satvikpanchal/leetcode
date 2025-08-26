class Solution:
    def isValid(self, s: str) -> bool:
        # if len(s) == 1:
        #     return False
        hash_map = {')': '(', ']': '[', '}': '{'}
        stack = []

        for i in s:
            if i in hash_map:
                if stack and stack[-1] == hash_map[i]:
                    stack.pop()
                else:
                    return False 
            else:
                stack.append(i)
        
        if len(stack) == 0:
            return True
        else:
            return False