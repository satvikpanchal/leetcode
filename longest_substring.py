# # first attempt

# from collections import defaultdict

# class Solution:
#     def lengthOfLongestSubstring(self, s: str) -> int:
#         substrings = []
#         cur_freq_dict = defaultdict(int)

#         if len(s) == 1:
#             return 1

#         for i in s:
#             if i not in cur_freq_dict:
#                 cur_freq_dict[i] = 1
#             else:
#                 substrings.append(cur_freq_dict.copy())
#                 cur_freq_dict.clear()
#                 cur_freq_dict[i] = 1

#         if cur_freq_dict:
#             substrings.append(cur_freq_dict.copy())

#         print(substrings)

#         max_len = 0
#         for j in substrings:
#             max_len = max(len(j), max_len)

#         return max_len


# second attempt

subs_set = set()
l = 0

max_len = 0

for r in range(0, len(s)):
    while s[r] in subs_set:
        subs_set.remove(s[l])

        # Updating the left window thing
        l += 1

    subs_set.add(s[r])

    max_len = max(max_len, len(subs_set))

# return max_len