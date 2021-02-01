def ToBin(h):
    b = bin(int(h,16))[2:]
    b = "0"*(4*len(h)-len(b)) + b
    return [int(i) for i in b]