from DES import DES

cipher = DES()
ED = bool(int(input("Encrypt: 0, Decrypt: 1\n")))
key = input("Key: ")
text = input("Ciphertext: " if ED else "Plaintext: ")
iterations = int(input("number of iterations: "))
if ED:
    for dummy in range(iterations):
        text = cipher.Decrypt(text,key)
else:
    for dummy in range(iterations):
        text = cipher.Encrypt(text,key)
print(text)