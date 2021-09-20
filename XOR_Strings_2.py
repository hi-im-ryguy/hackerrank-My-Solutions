def strings_xor(s, t):
    res = ""
    for i in range(len(s)):
        if bool(int(s[i])) ^ bool(int(t[i])):
            res += '1'
        else:
            res += '0'

    return res

s = input()
t = input()
print(strings_xor(s, t))



