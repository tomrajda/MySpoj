while True:
    try:
        data = [float(num) for num in input().split()]
        index = data.index(max(data))
        c = data.pop(index)

        if sum(data) > c:
            print(1)
        else:
            print(0)
    except EOFError:
        break