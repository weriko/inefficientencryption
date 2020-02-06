

WORD = str(input())
KEY = str(input())
KEY = KEY*(len(WORD)//len(KEY))
def encrypt(word,key,isEncrypt=True):
    abc = []
    chars = [chr(i) for i in range(32,128)]
    for i in range(len(chars)):
        abc.append(chars[i:len(chars):1] + chars[:i:1])
    if isEncrypt:
        out = ""
        for i,x in enumerate(word):
            try:
                character = abc[abc[0].index(key[i])][abc[0].index(x)]
                out += character
            except:
                out += x
        return out
    else:
       
        out2=""
        for i,x in enumerate(word):
            try:
                temp = abc[0].index(key[i])

                character = abc[temp][abc[temp].index(abc[0][abc[temp].index(x)])]
                out2 += character
            except:
                out2+=x
        return out2
encrypted = encrypt(WORD,KEY,  isEncrypt=True)
decrypted = encrypt(encrypted,KEY,  isEncrypt=False)
print(f"Encrypted word > {encrypted}  //  Decrypting the same word >  {decrypted}")


