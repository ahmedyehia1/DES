from tables import IP,PC1,SHIFT,IP_1
from Bin import ToBin,ToInt
from Mangler import Mangler
from keyGen import keyGen

def show(mang,w=8):
    print(len(mang))
    for i in range(0,len(mang),w):
        print(mang[i:i+w],sep='\n')

class DES:
    def __propagation(self,plaintext,key):
        roundtext = plaintext.copy()
        for i,p in enumerate(IP):
            roundtext[i] = plaintext[p-1]
        Pkey = [0]*56
        for i,p in enumerate(PC1):
            Pkey[i] = key[p-1]
        lk , rk =  Pkey[:28],Pkey[28:]
        left , right = roundtext[:32] , roundtext[32:]
        for r in range(16):
            lk , rk , roundKey = keyGen(lk,rk,SHIFT[r])
            mang = Mangler(right,roundKey)
            left , right = right , [l ^ m for l,m in zip(left,mang)]
        roundtext = right + left
        for i,p in enumerate(IP_1):
            plaintext[i] = roundtext[p-1]
        return plaintext

    def Encrypt(self,plaintext,key):
        plaintext = ToBin(plaintext)
        key = ToBin(key)
        return hex(ToInt(self.__propagation(plaintext,key)))[2:].upper()

    def Decrypt(self,ciphertext,key):
        pass

cipher = DES()
plaintext = "FFFFFFFFFFFFFFFF"
key = "0000000000000000"
d = cipher.Encrypt(plaintext,key)
print(d)
d = cipher.Encrypt(d,key)
print(d)