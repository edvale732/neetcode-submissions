class Solution:
    def isPalindrome(self, s: str) -> bool:
        forwards = (''.join(char for char in s if char.isascii() and char.isalnum())).lower()
        backwards = forwards[::-1]
        print(backwards)
        if backwards == forwards:
            return True
        return False