while True:
    try:
        
        op_nums = input().split()

        if op_nums[0] == "+":
            print(int(op_nums[1]) + int(op_nums[2]))

        elif op_nums[0] == "-":
            print(int(op_nums[1]) - int(op_nums[2]))

        elif op_nums[0] == "*":
            print(int(op_nums[1]) * int(op_nums[2]))

        elif op_nums[0] == "/":
            print(int(op_nums[1]) / int(op_nums[2]))

        elif op_nums[0] == "%":
            print(int(op_nums[1]) % int(op_nums[2]))

    except EOFError:
        break
