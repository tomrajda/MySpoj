sum = 0
while True:
    try:
        number = input()
        sum += int(number)
        print(sum)
    except EOFError:
        break