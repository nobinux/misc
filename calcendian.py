# 符号付き絶対値
def endian_absolute(num, wordsize):
    base = bin(abs(num))[2:]
    padding_size = wordsize - len(base)
    positive_bin = '0' * padding_size + base
    new = list(positive_bin)
    if num < 0:
        if new[0] == '1':
            new[0] = '0'
        else:
            new[0] = '1'
    binary = ''.join(new)

    if int(binary[:8], 2) < int(binary[8:], 2):
        return "big endian result \n" + binary[8:] \
         + ' ' + binary[:8] + "\n" + "little endian result \n" + binary[:8] \
         + ' ' + binary[8:] + "\n"
    else:
        return "big endian result \n" + binary[:8] \
         + ' ' + binary[8:] + "\n" + "little endian result \n" + binary[8:] \
         + ' ' + binary[:8] + "\n"


# 2の補数
def endian_2_complement(num, wordsize):
    if num < 0:
        num = 2**wordsize+num
    base = bin(num)[2:]
    padding_size = wordsize - len(base)
    binary = '0' * padding_size + base

    if int(binary[:8], 2) < int(binary[8:], 2):
        return "big endian result \n" + binary[8:] + ' ' + binary[:8] + "\n" \
         + "little endian result \n" + binary[:8] + ' ' + binary[8:] + "\n"
    else:
        return "big endian result \n" + binary[:8] + ' ' + binary[8:] + "\n" \
         + "little endian result \n" + binary[8:] + ' ' + binary[:8] + "\n"


print("0 : ", endian_absolute(0, 16))
print("1 : ", endian_absolute(1, 16))
print("-1 : ", endian_absolute(-1, 16))
print("5 : ", endian_absolute(5, 16))
print("-5 : ", endian_absolute(-5, 16))
print("5000 : ", endian_absolute(5000, 16))
print("-5000 : ", endian_absolute(-5000, 16))

print(endian_2_complement(0, 16))
print(endian_2_complement(1, 16))
print(endian_2_complement(-1, 16))
print(endian_2_complement(5, 16))
print(endian_2_complement(-5, 16))
print(endian_2_complement(5000, 16))
print(endian_2_complement(-5000, 16))
