def get_len_of_str(s):
    length = 0
    for i in range(0,len(s)-1):
        count = 1
        for j in range(i+1, len(s)):
            if s[i] == s[j]:
                if length < count:
                    length = count
                    break
            else:
                count +=1
                if count == len(s):
                    length = count
    return length

print(get_len_of_str('abcdefghijklmnop'))