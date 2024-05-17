import heapq
import sys

n = int(input())
heap = []
result = []

datas = [int(i.strip()) for i in sys.stdin.readlines()]

for data in datas:
    if data==0:
        if heap:
            result.append(heapq.heappop(heap))
        else:
            result.append(0)
    else:
        heapq.heappush(heap, data)

for data in result:
    print(data)