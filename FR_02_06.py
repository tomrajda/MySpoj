ndwg = []
warp = []
nadwg = []

for _ in range(int(input())):

    data = input().split()
    bmi = float(int(data[1]) / ((int(data[2]) / 100) ** 2))

    if bmi < 18.5:
        ndwg.append(data[0])
        continue
    elif bmi > 18.4 and bmi < 25:
        warp.append(data[0])
        continue
    else:
        nadwg.append(data[0])
        continue

print(f"niedowaga")
for i in ndwg:
    print(i)

print(f"\nwartosc prawidlowa\n")
for i in warp:
    print(i)

print(f"nadwaga")
for i in nadwg:
    print(i)





