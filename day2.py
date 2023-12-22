import re

def main():
    f = open('inputday2.txt', 'r')

    sum = 0
    for game in f:
        game_number = int(game.split(':')[0].split()[-1])
        items = re.findall(r'(\d+\s\w+)', game)

        colors = {}
        for item in items:
            count, color = item.strip().split()
            count = int(count)
            if color not in colors or count > colors[color]:
                colors[color] = count
        
        blue = colors['blue']
        red = colors['red']
        green = colors['green']

        if blue <= 14 and red <= 12 and green <= 13:
            sum += game_number

    print (sum)
    f.close()
main()