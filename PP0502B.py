def rev(nums):
    i_nums = [int(num) for num in nums.split()]
    i_nums.pop(0)
    i_nums.reverse()
    for num in i_nums:
        print(num)

for _ in range(int(input())):
    rev(input())