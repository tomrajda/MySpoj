for _ in range(int(input())):

    data = [(int(num) / 100) for num in input().split()]

    print('%.2f' % ((1 - ((1-data[0]) * (1-data[1]))) * 100))

