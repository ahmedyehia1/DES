from Bin import ToBin
from tables import PC2

def keyGen(left,right,shift):
    left = left[shift:] + left[:shift]
    right = right[shift:] + right[:shift]
    key = left+right
    roundKey = []
    for p in PC2:
        roundKey.append(key[p-1])
    return left, right, roundKey