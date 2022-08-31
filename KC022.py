while True:
    try:
        try:
            data = [int(num) for num in input().split()]
            rank = data.pop(0)
            sort_data = sorted(data, reverse=True)
            sort_data = list(dict.fromkeys(sort_data))
            print(sort_data[rank-1])
        except IndexError:
            print("-")
    except EOFError:
        break

#https://pl.spoj.com/problems/KC022/
