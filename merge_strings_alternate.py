class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        stack1 = []
        stack2 = []

        for i in word1[::-1]:
            stack1.append(i)

        for j in word2[::-1]:
            stack2.append(j)

        final_string = ""

        while True:
            if len(stack1) != 0:
                final_string += stack1.pop()

            if len(stack2) != 0:
                final_string += stack2.pop()

            if len(stack1) == 0 and len(stack2) == 0:
                break

        return final_string

        

        