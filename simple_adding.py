from unittest import result


iterations = int(input())

for _ in range(1, iterations+1):
    sum = 0
    numbers = input().split()
    for number in numbers:
        sum += int(number)
    res = sum / len(numbers)
    print(round(res))