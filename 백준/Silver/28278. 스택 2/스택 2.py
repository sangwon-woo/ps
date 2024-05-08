import queue
import sys
input=sys.stdin.readline

stack = queue.LifoQueue()
for i in range(int(input())):
    order = input().strip()
    if len(order) > 1:
        a, b = map(int, order.split(' '))
        stack.put(b)
        continue
    
    if order == '2':
        if not stack.empty():
            print(stack.get())
        else:
            print(-1)
    
    elif order == '3':
        print(stack.qsize())
    
    elif order == '4':
        if stack.empty():
            print(1)
        else:
            print(0)
    
    elif order == '5':
        if not stack.empty():
            a = stack.get()
            print(a)
            stack.put(a)
        else:
            print(-1)
