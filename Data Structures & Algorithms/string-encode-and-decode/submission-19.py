class Solution:

    def encode(self, strs: List[str]) -> str:
        str1 = ""
        for strn in strs:
            str1 += str(len(strn))
            str1 += "#"
            str1 += strn
        return(str1)
    def decode(self, s: str) -> List[str]:
        answer = []
        while s:
            length = ""
            while s[0] != "#":
                length += s[0]
                s = s[1:]
            sub = ""
            s = s[1:]
            l = int(length)
            sub = s[0:l]
            answer.append(sub)
            s = s[l:]
        return answer 