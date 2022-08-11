while True:
    try:
        nums = [float(num) for num in input().split()]
        d = (nums[1] ** 2) - 4 * (nums[0] * nums[2])
        if d > 0:
            print(2)
        elif d == 0:
            print(1)
        else:
            print(0)
    except EOFError:
        break

    


