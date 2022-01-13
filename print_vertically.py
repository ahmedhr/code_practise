from typing import List


def printVertically(s: str) -> List[str]:
    opt = []
    pointer = 0
    i = 0
    c = 0
    while pointer <= len(s)-1:
        if s[pointer] == " ":
            # for middle spaces
            #when space add blanks at the end of all words, since there are more words in the master string
            for q, new in enumerate(opt):
                new_len = len(opt[q])
                if new_len < c:
                    for i in range(c - new_len):
                        opt[q] += " "
            i = 0
            pointer += 1
            continue
        if len(opt)-1 >= i:
            opt[i] += s[pointer]
        elif len(opt)-1 < i:
            opt.append(s[pointer])
            #for pre-prend spaces
            # when length of current word is less than all words, prepend blank
            if len(opt) > 1 and len(opt[i]) < len(opt[i-1]):
                opt[i] = ""
                for sp in range(len(opt[i-1])-1):
                    opt[i] += " "
                opt[i] += s[pointer]
        if len(opt[i]) > c:
            c = len(opt[i])
        i += 1
        pointer += 1


    for i, n in enumerate(opt):
        opt[i] = opt[i].rstrip()

    return opt


s = "CONTEST IS COMING"

print(printVertically(s))


s = "TO BE OR NOT TO BE"

print(printVertically(s))



#method two
#split over spaces
#max length
#loop over max length and nest it with words loop 
#add letter if 'i' is less than length word length or add space