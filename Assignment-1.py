def sub_str(s,x):
    sub_str = []
    for i in range(len(s)):
        for j in range(i + x - 1, len(s)):
            if s[i] == s[j]:
                l = j - i + 1
                if l >= x:
                    sub_str.append(s[i:j + 1])
    min_len = min(len(substr) for substr in sub_str)
    min_str = [substr for substr in sub_str if len(substr) == min_len]
    for substr in min_str:
        print(substr)
s = "abccdbacca"
x = int(input("Enter an integer: "))
sub_str(s,x)
