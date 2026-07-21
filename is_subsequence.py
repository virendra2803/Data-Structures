
def issub(s,t):
    for i in s:
        if i in t:
            a = t.index(i)
            t = t[a + 1:]
        elif i not in t:
            return False
    return True
s = "abc"
t = "ahbgdc"

print(issub(s,t))

b = "asdfghjkl"

print(b[1:])

