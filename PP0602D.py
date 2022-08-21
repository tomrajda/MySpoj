nums = [int(num) for num in input().split()]

seq = input().split()

p1 = seq[:nums[1]]
p2 = seq[-(nums[0] - nums[1]):]

print(" ".join(p2 + p1))
    





