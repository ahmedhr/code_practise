# Input: name = "alex", typed = "aaleex"
# Output: true
# Explanation: 'a' and 'e' in 'alex' were long pressed.

# Input: name = "saeed", typed = "ssaaedd"
# Output: false
# Explanation: 'e' must have been pressed twice, but it wasn't in the typed output.


#
#
def isLongPressedName(name: str, typed: str) -> bool:
    c = 0
    tar_map = {}
    for i in name:
        if i != tar_map.get(len(tar_map), [0])[0]:
            c += 1
            tar_map[c] = [i, 1]
        else:
            tar_map[c][1] += 1
    c1 = 0
    ty_map = {}
    for i in typed:
        if i != ty_map.get(len(ty_map), [0])[0]:
            c1 += 1
            ty_map[c1] = [i, 1]
        else:
            ty_map[c1][1] += 1
    if c != c1:
        return False
    lent = max(c, c1)
    for i in range(lent):
        if ty_map[i + 1][0] != tar_map[i + 1][0]:
            return False
        if ty_map[i + 1][1] < tar_map[i + 1][1]:
            return False

    return True

# Optimized two pointer Solution
# def isLongPressedName(name: str, typed: str) -> bool:
#     if name == typed:
#         return True
#     i = 0
#     for j in range(len(typed)):
#         if i < len(name) and name[i] == typed[j]:
#             i += 1
#         elif i and name[i - 1] == typed[j]:
#             continue
#         else:
#             return False
#     return i == len(name)
#

print(isLongPressedName("saeed", "ssaaedd"))
