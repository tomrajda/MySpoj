
writting = ""
for _ in range(int(input())):

    inpt = input().split()
    
    if inpt[0] == "DODAJ":
        writting += inpt[1]
    elif inpt[0] == "USUN":
        writting = writting[:-int(inpt[1])]
    elif inpt[0] == "ZAMIEN":
        if writting:
            writting = writting[:-1] + inpt[1]
        else:
            continue

print(writting)