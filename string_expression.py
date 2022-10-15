input = "1+2*3"

operators = ["+", "-", "*", "/"]

weigthage = ["*", "-", "+"]



stack = {}
for i in range(0, len(input)):
    if input[i] in operators:
        stack[i] = input[i]





for k, i in stack.items():
    exp = str(input[k - 1]) + str(i) + str(input[k + 1])
    print(exp)
    ans = exec(str(exp))
    print(ans)
    print(input)
