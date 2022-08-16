for _ in range(int(input())):
    nums = [int(num) for num in input().split()]
    res = []
    for i in range(1, nums[0]+1):
        if i % nums[1] == 0:
            if i % nums[2] != 0:
                res.append(str(i))
    print(" ".join(res))

#https://pl.spoj.com/problems/PP0601B/
