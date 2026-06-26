import re

class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = re.sub(r'[^a-z0-9]', '', s.lower())

        reverse = s[::-1]

        if s == reverse:
            return True
        else:
            return False