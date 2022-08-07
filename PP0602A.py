for _ in range(int(input())):
    nums = [int(num) for num in input().split()]
    nums.pop(0)
    
    for num in nums[1::2]:
        print(num)
    for num in nums[0::2]:
        print(num)