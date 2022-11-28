import string

letters = string.ascii_uppercase
number = "16 9 3 15 3 20 6 20 8 5 14 21 13 2 5 18 19 13 1 19 15 14"
number = [int(i) for i in number.split()]
flag = []
for i in number:
    flag.append(letters[i-1])
print(number)
print("".join(flag[:7])+"{"+"".join(flag[7:])+"}")