while True:
    try:
        op_nums = input().split()
        nums = [int(op_num) for op_num in op_nums[1::]]

        if op_nums[0] == "+":
            print(nums[0] + nums[1])
            continue

        if op_nums[0] == "-":
            print(nums[0] - nums[1])
            continue

        if op_nums[0] == "*":
            print(nums[0] * nums[1])
            continue

        if op_nums[0] == "/":
            print(nums[0] / nums[1])
            continue

        if op_nums[0] == "%":
            print(nums[0] % nums[1])
            continue

    except EOFError:
        break

#https://pl.spoj.com/problems/CALC/