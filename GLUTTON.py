import math

for _ in range(int(input())):
    inpt_1 = [int(num) for num in input().split()]
    inpt_2 = []
    time = 86400
    for _ in range(inpt_1[0]):
        inpt_2.append(int(input()))
    
    cookies = []
    for t in inpt_2:
        cookies.append(math.floor(time / t))
    
    print(math.ceil(sum(cookies) / inpt_1[1]))


    


