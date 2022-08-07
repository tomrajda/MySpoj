for _ in range(int(input())):
    num = input()

    attempts = 0
    if num != num[::-1]:
        while num != num[::-1]:
            num = str(int(num) + int(num[::-1]))
            attempts += 1
        print(f"{num} {attempts}")
    else:
        print(f"{num} {attempts}")



