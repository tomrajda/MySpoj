def closest(nums):
    #calculate average of input numbers
    int_nums = [int(num) for num in nums.split()]
    qua = int_nums.pop(0)
    avg = sum(int_nums) / qua
    res = max(int_nums)

    #looking for closest number to avg
    for int_num in int_nums:
        dif = abs(avg - int_num)
        if dif < res:
            clo = int_num
            res = dif
        if res == 0:
            print(int_num)
            return None
    print(clo)

for _ in range(int(input())):
    closest(input())

#https://pl.spoj.com/problems/PP0604A/