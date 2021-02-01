from tables import IP,IP_1
from ToBin import ToBin

# left = key[:28]
# right = key[28:]

class DES:
    def __propagation(self,plaintext,key):
        # plaintext: list of binary
        # key: list of lists of round keys
        roundtext = plaintext.copy()
        for i,p in enumerate(IP):
            roundtext[i] = plaintext[p-1]
        return roundtext

    def Encrypt(self,plaintext,key):
        plaintext = ToBin(plaintext)
        key = ToBin(key)
        return self.__propagation(plaintext,key)

    def Decrypt(self,ciphertext,key):
        pass

cipher = DES()
d = cipher.Encrypt("0123456789ABCDEF","0123456789ABCDEF")
