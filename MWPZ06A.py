for _ in range(int(input())):
    data = [int(num) for num in input().split()]
    result = abs((data[0] + data[1] - (data[1] * data [2])) / (data[2] - 1))
    print(round(result * 12))
