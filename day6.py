with open ("inputday6.txt") as f:
    lines = f.read().split("\n")
    lines = [[int(item) for item in line.split(':')[1].strip().split()] for line in lines]

    time = lines[0]
    distance = lines[1]

result = 1
for i in range(len(time)):
    k = 0
    ms = time[i]
    dst = distance[i]
    for hold in range(ms):
        foo = hold * (ms-hold)
        if foo > dst:
            k +=1
    result *= k

print(result)