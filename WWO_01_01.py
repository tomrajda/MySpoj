classes = input().split()

students = []
for _ in range(len(classes)):
    students += input().split()

girls = 0
boys = 0
for name in students:
    if name[-1] == 'a':
        girls += 1
    else:
        boys += 1

print(min(girls, boys))



