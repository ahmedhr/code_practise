from typing import List

words = ["abc", "deq", "mee", "aqq", "dkd", "ccc"]

pattern = "abc"


def findAndReplacePattern(words: List[str], pattern: str) -> List[str]:
    pat_list = list()
    pat_set = dict()
    i = 0
    for p in pattern:
        if p not in pat_set:
            i += 1
            pat_set[p] = i
        pat_list.append(pat_set[p])
    ans = []
    for word in words:
        word_list = list()
        word_set = dict()
        i = 0
        for w in word:
            if w not in word_set:
                i += 1
                word_set[w] = i
            word_list.append(word_set[w])
        if pat_list == word_list:
            ans.append(word)
    return ans


print(findAndReplacePattern(words,pattern))