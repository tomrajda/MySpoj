iterations = int(input())

for _ in range(1, iterations+1):
    nums = input().split()
    number = int(nums[0][-1])
    if int(nums[1]) % 4 == 1:
        print(int(str(number)[-1]))
    elif int(nums[1]) % 4 == 2:
        print(int(str(number**2)[-1]))
    elif int(nums[1]) % 4 == 3:
        print(int(str(number**3)[-1]))    
    elif int(nums[1]) % 4 == 0:
        print(int(str(number**4)[-1]))
