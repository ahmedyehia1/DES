from tables import IP,PC1,SHIFT,IP_1
from Bin import ToBin,ToInt
from Mangler import Mangler
from keyGen import keyGen

def show(mang,w=8):
    print(len(mang))
    for i in range(0,len(mang),w):
        print(mang[i:i+w],sep='\n')

class DES:
    def __propagation(self,plaintext,roundKeys):
        roundtext = plaintext.copy()
        for i,p in enumerate(IP):
            roundtext[i] = plaintext[p-1]
        left , right = roundtext[:32] , roundtext[32:]
        for r in range(16):
            mang = Mangler(right,roundKeys[r])
            left , right = right , [l ^ m for l,m in zip(left,mang)]
        roundtext = right + left
        for i,p in enumerate(IP_1):
            plaintext[i] = roundtext[p-1]
        return plaintext

    def Encrypt(self,plaintext,key):
        plaintext = ToBin(plaintext)
        key = ToBin(key)
        roundKeys = []
        Pkey = [0]*56
        for i,p in enumerate(PC1):
            Pkey[i] = key[p-1]
        lk , rk =  Pkey[:28],Pkey[28:]
        for r in range(16):
            lk , rk , roundKey = keyGen(lk,rk,SHIFT[r])
            roundKeys.insert(-1,roundKey)
        return hex(ToInt(self.__propagation(plaintext,roundKeys)))[2:].upper()

    def Decrypt(self,ciphertext,key):
        ciphertext = ToBin(ciphertext)
        key = ToBin(key)
        roundKeys = []
        Pkey = [0]*56
        for i,p in enumerate(PC1):
            Pkey[i] = key[p-1]
        lk , rk =  Pkey[:28],Pkey[28:]
        for r in range(16):
            lk , rk , roundKey = keyGen(lk,rk,SHIFT[r])
            roundKeys.insert(0,roundKey)
        return hex(ToInt(self.__propagation(ciphertext,roundKeys)))[2:].upper()

cipher = DES()
plaintext = "abcdef1221abcdef"
key = "0000000000000000"
ciphertext = cipher.Encrypt(plaintext,key)
print(ciphertext)
plaintext = cipher.Decrypt(ciphertext,key)
print(plaintext)