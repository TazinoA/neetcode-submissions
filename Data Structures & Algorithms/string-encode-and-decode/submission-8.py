class Solution:

    def encode(self, strs: List[str]) -> str:
        if not strs:
            return ""
        if not strs[0] and len(strs) == 1:
            return " "
        return " T ".join(strs)

    def decode(self, s: str) -> List[str]:
        if not s:
            return []
        if s == " ":
            return [""]
        return s.split(" T ")
