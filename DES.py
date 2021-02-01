from tables import IP,PC1,SHIFT,IP_1
from Bin import ToBin,ToInt
from Mangler import Mangler
from keyGen import keyGen

def show(mang,w=8):
    print(len(mang))
    for i in range(0,len(mang),w):
        print(mang[i:i+w],sep='\n')

class DES:
    def __propagation(self,plaintext,key,direction):
        plaintext = ToBin(plaintext)
        key = ToBin(key)
        roundKeys = []
        Pkey = [0]*56
        for i,p in enumerate(PC1):
            Pkey[i] = key[p-1]
        lk , rk =  Pkey[:28],Pkey[28:]
        for r in range(16):
            lk , rk , roundKey = keyGen(lk,rk,SHIFT[r])
            roundKeys.insert(direction,roundKey)
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
        return hex(ToInt(self.__propagation(plaintext,key,-1)))[2:].upper()

    def Decrypt(self,ciphertext,key):
        return hex(ToInt(self.__propagation(ciphertext,key,0)))[2:].upper()

cipher = DES()
plaintext = "0000000000000000"
key = "FFFFFFFFFFFFFFFF"
ciphertext = cipher.Encrypt(plaintext,key)
print(ciphertext)
plaintext = cipher.Decrypt(ciphertext,key)
print(plaintext)