counter = 0
while True:
    try:
        line = input()
        counter += 1
    except EOFError:
        print(counter)
        break
        