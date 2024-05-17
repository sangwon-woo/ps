import heapq
import sys

n = int(input())
heap = []
result = 0

datas = [int(i.strip()) for i in sys.stdin.readlines()]

for data in datas:
    heapq.heappush(heap, data)

while len(heap) != 1:
    one = heapq.heappop(heap)
    two = heapq.heappop(heap)
    sum_value = one+two
    result += sum_value
    heapq.heappush(heap, sum_value)

print(result)