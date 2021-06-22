##check if whole code_list exists in cart list consecutively


code_list = ["app", "oos", "jos"]

cart_list = ["asasas", "app", "oos", "jos"]

blen = len(cart_list)
alen = len(code_list)


def sol():
    if alen > blen:
        return 0
    j = 0
    start = 0
    for i in range(blen):
        if alen <= j:
            continue
        if cart_list[i] == code_list[j]:
            j += 1
            start = 1
            cont = 1
        else:
            cont = 0
        if start ^ cont:
            return 0
    if j + 1 == alen:
        return 0
    return 1


print(sol())
