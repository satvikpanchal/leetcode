# first attempt

from collections import defaultdict

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        substrings = []
        cur_freq_dict = defaultdict(int)

        if len(s) == 1:
            return 1

        for i in s:
            if i not in cur_freq_dict:
                cur_freq_dict[i] = 1
            else:
                substrings.append(cur_freq_dict.copy())
                cur_freq_dict.clear()
                cur_freq_dict[i] = 1

        if cur_freq_dict:
            substrings.append(cur_freq_dict.copy())

        print(substrings)

        max_len = 0
        for j in substrings:
            max_len = max(len(j), max_len)

        return max_len
