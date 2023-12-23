from collections import defaultdict

def main():
    with open("inputday4.txt") as f:
        data = f.read()
        lines = data.splitlines()
    #dict to keep count of each cards
    N = defaultdict(int)
    for i, line in enumerate(lines):
        #default card
        N[i] += 1

        win_num = line.split(':')[1].split('|')[0].split()
        win_num = [int(num) for num in win_num]
        my_num = line.split('|')[1].split()
        my_num = [int(num) for num in my_num]

        matches = sum(1 for num in win_num if num in my_num)

        #depending on matches it adds copies to the dict
        for j in range(matches):
            N[i+1+j] += N[i]
    print(sum(N.values()))
main()
