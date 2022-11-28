import string

LOWERCASE_OFFSET = ord("a")
ALPHABET = string.ascii_lowercase[:16]


def b16_encode(plain):
    encryption = ""
    for curLetter in plain:
        binary = "{0:08b}".format(ord(curLetter))
        encryption += ALPHABET[int(binary[:4], 2)]
        encryption += ALPHABET[int(binary[4:], 2)]
    return encryption


def b16_decode(plain):
    msg = ""
    for charIndex in range(0, len(plain), 2):
        cur1 = ALPHABET.find(plain[charIndex])
        cur2 = ALPHABET.find(plain[charIndex + 1])
        cur1 = "{0:04b}".format(cur1)
        cur2 = "{0:04b}".format(cur2)
        binar = cur1 + cur2
        binar = int(binar, 2)
        msg += chr(binar)
    return msg


def shift(c, k):
    t1 = ord(c) - LOWERCASE_OFFSET
    t2 = ord(k) - LOWERCASE_OFFSET
    return ALPHABET[(t1 + t2) % len(ALPHABET)]


def restoreShift(c, k, key):
    d = ALPHABET.find(c)
    i = key[k % len(key)]
    t = ord(i) - LOWERCASE_OFFSET
    d = chr((d - t) % len(ALPHABET) + LOWERCASE_OFFSET)
    return d

flag = "redacted"
key = "redacted"

b16 = b16_encode(flag)
enc = ""
for i, c in enumerate(b16):
    enc += shift(c, key[i % len(key)])
print(enc)

encryptionCTF = "kjlijdliljhdjdhfkfkhhjkkhhkihlhnhghekfhmhjhkhfhekfkkkjkghghjhlhghmhhhfkikfkfhm"

for m in ALPHABET:
    clearCTF = ""
    for i,c in enumerate(encryptionCTF):
        clearCTF += restoreShift(c, i, m)
    print(b16_decode(clearCTF))
