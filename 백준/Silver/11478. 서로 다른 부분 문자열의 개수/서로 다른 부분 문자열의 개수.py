string = [i for i in input()]
ans = set()

string_len = len(string)
for n in range(1, string_len+1):
    end_idx = string_len -n
    for i in range(end_idx+1):
        w = ''.join(string[i:i+n])
        ans.add(w)
print(len(ans))