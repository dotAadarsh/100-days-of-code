# min number needed to mane string palindrome

def pali(s):
    n = len(s)
    k = 0

    for i in range(n-1, n//2, -1):
        if s[i] != s[k]:
            s += s[k]
            k += 1
        else:
            k+=1

    print(k)

string = "aabb"
pali(string)
