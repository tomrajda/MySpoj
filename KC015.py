while True:
    try:
        data = input().split()
        sym = data.pop(1)

        data = [int(num) for num in data]

        if sym == "==":
            if data[0] == data[1]:
                print(1)
            else:
                print(0)
            continue
        elif sym == "!=":
            if data[0] != data[1]:
                print(1)
            else:
                print(0)    
            continue    
        elif sym == "<=":
            if data[0] <= data[1]:
                print(1)
            else:
                print(0)
            continue        
        elif sym == ">=":
            if data[0] >= data[1]:
                print(1)
            else:
                print(0)
            continue        
        elif sym == ">":
            if data[0] > data[1]:
                print(1)
            else:
                print(0)
            continue       
        elif sym == "<":
            if data[0] < data[1]:
                print(1)
            else:
                print(0)
            continue
    except EOFError:
        break