##find the first and last digit of the string then combine them, repeat for every string 
##and lastly sum all numbers

def main():
    sum = 0
    f = open("input.txt","r")
    #f = ["abc123def456","l4o9e"]
    for string in f:
        first_digit = None
        last_digit = None
        for char in string:
            if char.isdigit():
                first_digit = char
                break
        for i in range(len(string)-1, -1, -1):
            if string[i].isdigit():
                last_digit = string[i]
                break
        string_number= int(first_digit + last_digit)
        sum += string_number

    f.close()
    print(sum)


main()