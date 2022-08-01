iterations = int(input())

for _ in range(1, iterations+1):
    result = 0
    n = int(input())
    numbers = input().split()
    for _ in range(n):
        number = numbers.pop(0)
        result += int(number)
    print(result)