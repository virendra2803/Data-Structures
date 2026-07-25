#valid parantheses
s = "()[(]{}"

def vaild_para(s):
    map = { "}":"{","]":"[",")":"("}

    stack = []
    for i in s:
        if i in map.values():
            stack.append(i)
        elif i in map:
            if not stack or stack[-1] != map[i]:
                return False
            stack.pop()
        else:
            return False
    return not stack

print(vaild_para(s))