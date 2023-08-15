def str_ing(s):
    nstr = list(s)
    index = set()    
    for i in range(len(s)):
        ascii_value = ord(s[i])
        if ascii_value%2 == 0  and i < len(s) - 1 and ord(nstr[i]) >= 32:
                nascii = (ascii_value + (ascii_value % 7))
                nstr[i+1] = chr(nascii)
                index.add(i+1)
        elif i > 0 and ord(nstr[i]) <= 32:
                nascii = (ascii_value - (ascii_value % 5))
                nstr[i-1] = chr(nascii)
                index.add(i-1)
        elif ord(nstr[i]) <= 32:
            nstr[i+1] = chr(83)
    return ''.join(nstr)
s = str(input("Enter a string: "))
new_str = str_ing(s)
print(new_str)
