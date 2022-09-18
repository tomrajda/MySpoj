for _ in range(int(input())):

    week = [
            "Pn", "Wt", "Sr", "Cz", 
            "Pt", "So", "Nd"
            ]
    data = input().split()
    d = int(data[1]) % 7
    if d == 0:

        print(data[0])

    else:

        i = week.index(data[0]) + int(data[1])
        if i < 7:

            print(week[i])
            continue

        else:

            f = i % 7
            print(week[f])





