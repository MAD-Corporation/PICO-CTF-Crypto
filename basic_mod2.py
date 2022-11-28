import string

flag = ""
alphaNumeric = string.ascii_lowercase + string.digits + "_"
encryptMsg = [int(i) % 41 for i in
              "104 85 69 354 344 50 149 65 187 420 77 127 385 318 133 72 206 236 206 83 342 206 370".split()]
for j in encryptMsg:
    reach = False
    n = 1
    while not reach:
        if (n * j) % 41 == 1:
            reach = True
            flag += alphaNumeric[n - 1]
        else:
            n += 1

print(flag)
