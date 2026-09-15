class Solution:
    def isValid(self, s: str) -> bool:
        bracket_map = {")": "(", "}": "{", "]": "["}
        bracket = []
        for b in s:
            if b in bracket_map.values():
                bracket.append(b)
            elif b in bracket_map:
                if not bracket or bracket.pop() != bracket_map[b]:
                    return False
        if not bracket:
            return True
        return False
            