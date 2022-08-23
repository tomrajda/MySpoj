while True:
    try:
        print(input().title().replace(" ", ""))
    except EOFError:
        break