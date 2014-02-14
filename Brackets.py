# 100 https://codility.com/c/run/demoFGZJ4D-PXV
# Had to rely on http://codesays.com/2014/solution-to-brackets-by-codility/

def solution(S):
    matched = {')': '(', ']': '[', '}': '{'}
    stack = []

    for char in S:                  # an open bracket
        if char in matched.values():
            stack.append(char)
        else:                       # a closed bracket
            if len(stack) == 0:
                return 0
            if matched[char] != stack.pop():
                return 0
    if len(stack) == 0:
        return 1
    else:
        return 0
            
print solution('{[()()]}')
print solution('{}[()()]')
print solution('{)}[()()]')
