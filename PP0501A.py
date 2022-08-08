def nwd(nums):
    i_nums = [int(num) for num in nums.split()]
    a = i_nums[0]
    b = i_nums[1]
    while b != 0:
        temp = b
        b = a % b
        a = temp
    print(a)

for _ in range(int(input())):
    nwd(input())