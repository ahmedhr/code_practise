from collections import defaultdict


def partitionLabels(s: str) -> list[int]:
    letter_range = defaultdict(dict)
    for i, n in enumerate(s):
        if letter_range[n].get("last"):
            letter_range[n]["last"] = i
        else:
            letter_range[n]["first"] = i
            letter_range[n]["last"] = i

    partition = []
    last_index = letter_range[s[0]]["last"]
    previous_partition = 0
    for i, n in enumerate(letter_range):
        if letter_range[n]["first"] > last_index:
            p = last_index+1 - previous_partition if previous_partition else last_index + 1
            partition.append(p)
            previous_partition += p
            last_index = letter_range[n]["last"]

        if letter_range[n]["first"] < last_index and letter_range[n]["last"] > last_index:
            last_index = letter_range[n]["last"]

    partition.append(last_index+1 - previous_partition)


s = "abcdefghija"

partitionLabels(s)



def partitionLabels(s: str) -> list[int]:
    letter_range = defaultdict()
    for i, n in enumerate(s):
        letter_range[n] = i
    
    partition = []

    i = 0 
    while i < len(s):
        end = letter_range[s[i]]
        j = i + 1
        while (j != end):
            if letter_range[s[j]] > end:
                end = letter_range[s[j]]
            j += 1
        partition.append(j - i +1)
        i = j + 1
    print(partition)

s = "ababcbacadefegdehijhklij"

partitionLabels(s)
