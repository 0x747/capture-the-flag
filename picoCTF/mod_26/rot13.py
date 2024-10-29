import sys

encoded_flag = "cvpbPGS{arkg_gvzr_V'yy_gel_2_ebhaqf_bs_ebg13_hyLicInt}"

flag = ''

for c in encoded_flag:
    offset = 65 if c.isupper() else 97
    flag += chr((ord(c) + 13) % 26 + offset)

print(flag)