from tables import EP,SBOX,P
from Bin import ToBin,ToInt

def Mangler(right,key):
    plaintext = [0]*48
    for i,p in enumerate(EP):
        plaintext[i] = right[p-1]
    plaintext = [p ^ k for p,k in zip(plaintext,key)]
    plaintext = [plaintext[i:i+6] for i in range(0,len(plaintext),6)]
    plaintext = [(ToInt([element[0],element[-1]]),ToInt(element[1:-1])) for element in plaintext]
    plaintext = [SBOX[i][element[0]][element[1]] for i,element in enumerate(plaintext)]
    plaintext = sum([ToBin(hex(element)[2:]) for element in plaintext],[])
    output = plaintext.copy()
    for i,p in enumerate(P):
        output[i] = plaintext[p-1]
    return output
