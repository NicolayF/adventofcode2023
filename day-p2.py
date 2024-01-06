with open ("inputday6.txt") as f:
    lines = f.read().split("\n")
    lines = [''.join(line.split(':')[1].strip().split()) for line in lines]

    time = int(lines[0])
    distance = int(lines[1])

k = 0
for hold in range(time):
    foo = hold * (time-hold)
    if foo <= distance:
        k +=1
    else:
        continue

print(time-k)

