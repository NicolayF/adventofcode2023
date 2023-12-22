import re


def main():
    sum = 0
    #f = "xtwone3four0"
    f = open("inputday1-p2.txt","r")
    all_digits = {'zero':'0', 'one':'1', 'two':'2', 'three':'3', 'four':'4', 'five':'5',
                  'six':'6', 'seven':'7', 'eight':'8', 'nine':'9' }
    
    regex = r'(?=(zero|one|two|three|four|five|six|seven|eight|nine|\d))'
    for string in f:
        extract = re.findall(regex , string)

        digits = [all_digits[word] if word in all_digits else word for word in extract]

        #print(extract)
        #print(digits)
        sum += int(digits[0] + digits[-1])

    f.close()
    print(sum)

main()