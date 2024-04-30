for _ in range(int(input())):
    h, w, n = map(int, input().split())
    story = n%h
    room_number = 1 + n//h
    if story == 0:
        room_number -= 1
        story = h
        
    room_number = str(room_number) if room_number > 9 else '0' + str(room_number)
    ret = str(story) + room_number
    print(ret)