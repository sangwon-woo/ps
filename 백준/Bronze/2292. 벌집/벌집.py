n = int(input())

ss = 0
cnt = 1
while 1:
    temp = 6*(cnt-1) if cnt > 1 else 1
    if temp + ss >= n:
        print(cnt)
        break
    cnt += 1
    ss += temp
    