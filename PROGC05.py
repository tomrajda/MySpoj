
while True:
    try:
        data = input().split()
        res = ""
        for i in data[1]:
            if i != data[0]:
                res += i
        print(res)
    except EOFError:
        break

#https://pl.spoj.com/problems/PROGC05/
        