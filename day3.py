

def main():
    with open("inputday3.txt") as f:
        data = f.read()
        lines = data.splitlines()


    coords_s = set()
    #get indexes
    for r, row in enumerate(lines):
        for c, char in enumerate(row):
            #skip non-symbols
            if char.isdigit() or char == '.':
                continue
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
    
    numbers_l = []
    for r, c in coords_s:
        nums = ""
        #get the entire number
        while c < len(lines[r]) and lines[r][c].isdigit():
            nums += lines[r][c]
            c += 1
        numbers_l.append(int(nums))

    print(sum(numbers_l))


main()