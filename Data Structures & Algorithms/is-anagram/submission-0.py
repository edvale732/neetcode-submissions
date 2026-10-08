class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        s_dict = {}
        for char in s:
            s_dict[char] = s_dict.get(char, 0) + 1

        t_dict = {}
        for t_char in t:
            t_dict[t_char] = t_dict.get(t_char, 0) + 1

        return s_dict == t_dict
