while True:
    try:
        
        data = [int(num) for num in input().split()]
        c = data.pop(data.index(max(data)))
        if sum(data) > c:

            if data[0] ** 2 + data[1] ** 2 == c ** 2:

                print("prostokatny")
                continue

            if data[0] ** 2 + data[1] ** 2 < c ** 2:

                print("rozwartokatny")
                continue

            if data[0] ** 2 + data[1] ** 2 > c **2:

                print("ostrokatny")
                continue
        else:

            print("brak")

    except EOFError:
        break
    


