# Valid Parenthesis - https://leetcode.com/problems/valid-parentheses/

def isValid(s):
  stack = []
  parenthesis = {
    '(':')',
    '[':']',
    '{':'}'
  }
  s = [e for e in s]
      
  while s:
    if len(stack)!=0:
      if s[0] == parenthesis.get(stack[-1]):
        s.pop(0)
        stack.pop(-1)
      else:
        stack.append(s.pop(0))
    else:
      stack.append(s.pop(0))
              
  return False if stack else True

s1 = "()[]{}"
s2 = "(]"

print(isValid(s1))
print(isValid(s2))

