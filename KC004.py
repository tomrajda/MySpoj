while True:
    try:
        data = [int(num) for num in input().split()]
        j = data.pop(0)
        counter = 0
        
        for i in data[1:]:
            if i == j:
                counter += 1
        print(counter)
    except EOFError:
        break