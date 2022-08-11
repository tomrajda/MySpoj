for _ in range(int(input())):
    inpt_1 = [int(num) for num in input().split()]
    inpt_1.pop(0)
    inpt_1.append(inpt_1.pop(0))
    for x in inpt_1:
        print(x)

    


