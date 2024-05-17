import heapq

n, m = map(int, input().split())
array = [[] for i in range(n+1)]
indegree = [0] * (n+1) # 진입차수
heap = []
result = []

for _ in range(m):
    x, y = map(int, input().split())
    array[x].append(y) # x번 문제를 y번 문제보다 먼저 푼다.
    indegree[y] += 1 # y번 문제의 진입 차수 하나 추가


for i in range(1, n+1): # 쉬운 문제부터 보면서 진입차수가 있는지 확인
    if indegree[i] == 0: # 진입차수가 없으면 heap에다 넣기
        heapq.heappush(heap, i)
    
while heap:
    data = heapq.heappop(heap)
    result.append(data)
    for y in array[data]:
        indegree[y] -= 1
        if indegree[y] == 0:
            heapq.heappush(heap, y)

[print(i, end=' ') for i in result]