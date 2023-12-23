

def main():
    with open("inputday3.txt") as f:
        data = f.read()
        lines = data.splitlines()

    total = 0
    #get indexes
    for r, row in enumerate(lines):
        for c, char in enumerate(row):
            #skip non-asterisks
            if char != '*':
                continue
            #unique coord set for each asterisk
            coords_s = set()
            #check area around the symbol
            for cr in [r - 1, r, r + 1]:
                for cc in [c - 1, c, c + 1]:
                    #skip if out of bounds
                    if cr < 0 or cr >= len(lines) or cc < 0 or cc >= len(lines[cr]) or not lines[cr][cc].isdigit():
                        continue
                    #find the coordinates to the first digit of the number
                    while cc > 0 and lines[cr][cc - 1].isdigit():
                        cc -= 1
                    coords_s.add((cr, cc))
            #skip if we don't have 2 numbers adjacent
            if len(coords_s) != 2:
                continue
    
            numbers_l = []
            for cr, cc in coords_s:
                nums = ""
                #get the entire number
                while cc < len(lines[cr]) and lines[cr][cc].isdigit():
                    nums += lines[cr][cc]
                    cc += 1
                numbers_l.append(int(nums))
            total += numbers_l[0] * numbers_l[1]
    print(total)


main()