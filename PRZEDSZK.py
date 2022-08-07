for _ in range(int(input())):
    nums = [int(num) for num in input().split()]
    v1 = max(nums)
    v2 = min(nums)

    for x in range(1, max(nums)):
        r = x * v1
        if r % v2 == 0:
            value = x * v1
            print(value)
            break

