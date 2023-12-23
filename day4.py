def main():
    with open("inputday4.txt") as f:
        data = f.read()
        lines = data.splitlines()
    
    total = 0
    for line in lines:
        win_num = line.split(':')[1].split('|')[0].split()
        win_num = [int(num) for num in win_num]
        my_num = line.split('|')[1].split()
        my_num = [int(num) for num in my_num]

        matches = sum(1 for num in win_num if num in my_num)
        if matches == 0:
            continue
        total += 2**(matches-1)
    print(total)

main()
