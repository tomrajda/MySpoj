for _ in range(int(input())):
    num = int(input())
    if num != 0:
        if num == 1:
            print("0 1")
        elif num == 2:
            print("0 2")
        elif num == 3:
            print("0 6")
        elif num == 4:
            print("2 4")
        elif num == 5 or num == 6 or num == 8:
            print("2 0")
        elif num == 7:
            print("4 0")
        elif num == 9:
            print("8 0")
        else:
            print("0 0")
    else:
        print("0 1")