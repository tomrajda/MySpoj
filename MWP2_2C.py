import math

for _ in range(int(input())):
    circle_1 = [int(num) for num in input().split()]
    circle_2 = [int(num) for num in input().split()]
    
    l = math.hypot(circle_1[0] - circle_2[0], circle_1[1] - circle_2[1])

    if l >= circle_1[2] + circle_2[2]:
        print("%0.2f" % 0)
        continue
    elif l > abs(circle_1[2] - circle_2[2]) and l < circle_1[2] + circle_2[2]:
        print("%0.2f" % (circle_1[2] + circle_2[2] - l))
        continue
    elif l <= abs(circle_1[2] - circle_2[2]):
        print("%0.2f" % (2 * (min(circle_1[2], circle_2[2]))))
        continue
    else:
        print("%0.2f" % (2 * (min(circle_1[2], circle_2[2]))))    
        continue   

