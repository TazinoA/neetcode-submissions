class Solution:
    def isValid(self, s: str) -> bool:
        if (len(s) % 2) != 0:
            return False
        stack = []
        opening = set({"(", "{", "["})
        brackets = {
            ")":"(",
            "}":"{",
            "]":"["
        }

        for bracket in s:
            if bracket in opening:
                stack.append(bracket)
            else:
                if len(stack) == 0 or stack.pop(-1) != brackets[bracket]:
                    return False
        return len(stack) == 0

        