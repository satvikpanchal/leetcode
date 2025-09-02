# first attempt

# subs_list = list(s)
# t_list = list(t)
# filtered = [ch for ch in t_list if ch in subs_list]
# print(subs_list)
# print(filtered)
# return filtered == subs_list if len(filtered) == len(subs_list) else False

# second attempt

i, j = 0, 0

while i < len(s) and j < len(t):
    if s[i] == t[j]:
        i += 1
        j += 1
    else:
        j += 1

if i == len(s):
    return True
else:
    return False
