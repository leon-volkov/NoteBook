n = 10

def isPalindrome(n):
    print(n, n == n[::-1], '<===' if n == n[::-1] else None)
    return n == n[::-1]

out = [0,0,0]
for i in range(10, n+1):
    p10 = isPalindrome(str(i))
    p2 = isPalindrome(bin(i)[2:])
    if p10 and p2:
        out[2] += 1
    elif p10:
        out[0] += 1
    elif p2:
        out[1] += 1

print(*out)
