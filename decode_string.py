def dec_str(s):
    ct_st = []
    str_st = []
    curr_str = ""
    curr_num = 0

    for i in s:
        if i.isdigit():
            curr_num = curr_num * 10 + int(i)
        elif i == "[":
            ct_st.append(curr_num)
            str_st.append(curr_str)
            curr_str = ""
            curr_num = 0
        
        elif i == "]":
            prev_str = str_st.pop()
            r_ct = ct_st.pop()

            curr_str = prev_str + (curr_str) * r_ct
        else:
            curr_str += i
    return curr_str

s = "2[abc]3[cd]ef"

print(dec_str(s))
