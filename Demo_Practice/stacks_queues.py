# Given a string s containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.

# An input string is valid if:

# Open brackets must be closed by the same type of brackets.
# Open brackets must be closed in the correct order.
# Every close bracket has a corresponding open bracket of the same type.
 
# class Solution(object):
#     def isValid(self, s):

#         stack = []

#         pairs = {
#             ')': '(',
#             ']': '[',
#             '}': '{'
#         }

#         for ch in s:

#             if ch in "([{":
#                 stack.append(ch)

#             else:
#                 if not stack:
#                     return False

#                 if stack[-1] != pairs[ch]:
#                     return False

#                 stack.pop()

#         return len(stack) == 0

# You are given a string s consisting of lowercase English letters. A duplicate removal consists of choosing two adjacent and equal letters and removing them.

# We repeatedly make duplicate removals on s until we no longer can.

# Return the final string after all such duplicate removals have been made. It can be proven that the answer is unique.

 
class Solution(object):
    def removeDuplicates(self, s):
        stack=[]
        for ch in s:
        
            if stack and stack[-1]==ch:
                stack.pop()
                
            else:
                stack.append(ch)
                
        return "".join(stack)
obj=Solution()
s = "abbaca"
print(obj.removeDuplicates(s))
