with open ("test.txt") as f:
    lines = f.read().strip().split("\n")
#print(lines)

seeds_raw = lines[0].split(" ")[1:]
seeds_pairs = list(map(int, seeds_raw))

seeds_list = []
for i in range(0, len(seeds_pairs), 2):
    seeds_list.append((seeds_pairs[i], seeds_pairs[i] + seeds_pairs[i+1]))
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

new = []
while len(seeds_list) > 0:
    ss, se = seeds_list.pop()
    for m in maps:
        for dst, src, range in m:
            os = max(ss, src)
            oe = min(se, src+range)
            if os < oe:
                new.append((os-src+dst, oe-src+dst))
                if os > ss:
                    seeds_list.append((ss, os))
                if se > oe:
                    seeds_list.append((oe, se))
                break
            else:
                new.append((ss, se))

#print(seeds_list)
#print(new)
print(min(new)[0])
