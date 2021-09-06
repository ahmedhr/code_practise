from collections import defaultdict

S = "adcvregtbgchbcrrewath"

W = "cat"

"""
Find how many W can be made from S
"""

count_s = defaultdict(int)
count_w = defaultdict(int)
for i in S:
    count_s[i] += 1

for j in W:
    count_w[j] += 1

alpha_count = None

for k in count_w:
    current_count = count_s[k] // count_w[k]
    try:
        if alpha_count > (current_count):
            alpha_count = current_count
    except:
        alpha_count = current_count


print(alpha_count)