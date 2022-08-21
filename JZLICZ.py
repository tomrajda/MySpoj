txt = ""
for _ in range(int(input())):
    
    txt += "".join(input().split())

lowers = []
uppers = []
for l in txt:
    
    if l not in "".join(lowers + uppers):
        
        if l.isupper() != True:
            
            counter = 0
            for k in txt:
                if k == l:
                    counter += 1
            result = f"{l} {counter}"
            lowers.append(result)

        else:

            counter = 0
            for k in txt:
                if k == l:
                    counter += 1
            result = f"{l} {counter}"
            uppers.append(result)            

lowers.sort()
uppers.sort()
letters = lowers + uppers
for i in letters:
    print(i)




