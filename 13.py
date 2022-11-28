import string

alphabet = string.ascii_lowercase
cipher = "cvpbPGS{abg_gbb_onq_bs_n_ceboyrz}"
clear  = ""
for i in cipher:
    if i in alphabet:
        ind = alphabet.find(i)
        ind = (ind-13)%(len(alphabet))
        i = alphabet[ind]
    clear += i

print(clear)