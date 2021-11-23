a = "893849"
b = "0"

print(int(a) * int(b))

a = a[::-1]
b = b[::-1]



results = []
count = 0
for i in a:
    carry = None
    ans = ""
    for j in b:
        res = int(i) * int(j) 
        if carry:
           res += carry
           carry = None
        if res > 10:
            carry = res // 10
            res = res % 10
        ans = str(res) + str(ans)
    if carry:
        ans = str(carry) + ans        
    for _ in range(count):
        ans = str(ans) + "0"
    results.append(ans)
    count += 1

print(results)
    
mul = "0"
for i in results:
   mul = str(int(mul) + int(i))

print(mul)