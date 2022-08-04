

def sum(nums):
    #sum of (PESEL numbers * multipers)
    int_nums = [int(num) for num in nums]
    multis = [1, 3, 7, 9]
    multis_1 = [1, 3, 1]
    
    sum = 0
    i = 0
    for _ in range(2):
        for multi in multis:
            sum += multi * int_nums[i]
            i += 1
    for multi_1 in multis_1:
        sum += multi_1 * int_nums[i]
        i += 1
    
    if sum > 0:
        if str(sum)[-1] == "0":
            print("D")
        else:
            print("N")
    else:
        print("N")

for _ in range(int(input())):
    sum(input())

#https://pl.spoj.com/problems/JPESEL/