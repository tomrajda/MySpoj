for _ in range(int(input())):
    data = [int(num) for num in input().split()]
    data[0] -= 1

    if data[0] == 0:
        print('TAK')
    elif data[1] % data[0] != 0:
        print('TAK')
    elif data[1] % data[0] == 0:
        print('NIE')

#https://pl.spoj.com/problems/MWPZ06D/