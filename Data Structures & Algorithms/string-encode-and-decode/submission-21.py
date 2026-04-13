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
        i = 0
        while i < len(s):
            j = i
            while s[j] != "#":
                j+=1
            length = int(s[i:j])
            answer.append(s[j+1:j+1+length])
            i = j+1+length
        return answer 