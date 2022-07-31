iterations = int(input())

for _ in range(1, iterations+1):
    number = int(input())
    divisors = 0
    if number == 1:
        print("NIE")
        continue
    for i in range(2, int(number**0.5)+1):
        if number % i == 0:
            divisors += 1
            if divisors == 1:
                break        
    if divisors == 1:
        print("NIE")
    else:
        print("TAK")
            