class Solution:
    def isPalindrome(self, s: str) -> bool:
        left = 0
        right = len(s) - 1
        while right > left:
            if not s[left].isalpha() and not s[left].isdigit():
                left += 1
                continue
            if not s[right].isalpha() and not s[right].isdigit():
                right -= 1
                continue
            if s[left].lower() == s[right].lower():
                left += 1
                right -= 1
            else:
                return False
        return True
                