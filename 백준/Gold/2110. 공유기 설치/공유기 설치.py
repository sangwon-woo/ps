import sys
input = sys.stdin.readline

N, C = map(int, input().split()) # house, router
house = [int(input()) for _ in range(N)]

house.sort()
start, end = 1, house[-1]-house[0]
while start <= end:
    mid = (start+end)//2
    current = house[0]
    cnt = 1
    # 공유기 설치 몇 대 할 수 있는지 체크
    for i in range(1, N):
        if house[i] - mid >= current:
            cnt += 1
            current = house[i]
    
    # 공유기 설치 수가 목표 보다 크면 공유기 사이 거리 늘림
    if cnt >= C:
        start = mid + 1
        result = mid
    # 공유기 설치 수가 목표 보다 작으면 공유기 사이 거리 줄임
    else:
        end = mid - 1

print(result)