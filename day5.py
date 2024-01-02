with open ("inputday5.txt") as f:
    lines = f.read().strip().split("\n")

#print(lines)
seeds = lines[0].split(" ")[1:]
seeds_list = list(map(int, seeds))

#print(seeds_list)
maps = []
i = 3
while i < len(lines):
    maps.append([])
    try: 
        while not lines[i] == "":
            dst, src , range = map(int, lines[i].split())
            maps[-1].append((dst, src, range))
            i += 1
    except:
        break
    i += 2
#print(maps)
    
def findLocation(seed):
    foo = seed
    for m in maps:
        for dst, src, range in m:
            if src <= foo and foo < src + range:
                foo = dst + (foo - src)
                break
    return foo

locs = []
for seed in seeds_list:
    loc = findLocation(seed)
    locs.append(loc)

print(min(locs))
