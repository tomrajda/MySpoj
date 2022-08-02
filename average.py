iterations = int(input())

if iterations < 101 and iterations > 0:
    for _ in range(1, iterations+1):
        sum = 0
        numbers = input().split()

        if all(int(i) < 100 for i in numbers):
            for number in numbers:
                sum += int(number)
            res = sum / len(numbers)
            print(round(res))
        else:
            break