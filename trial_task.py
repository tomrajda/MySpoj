sum = 0
for _ in range(2):
    number = int(input())
    if number < 200:
        sum += number
    else:
        break
print(sum)