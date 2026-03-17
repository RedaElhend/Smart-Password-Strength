# this just a code you will need to instal rockyou.txt to run it with this

import string
import time

# make chore the code have more or 8 caractair
while True:
    code=input("chose a password :")
    if len(code)>=8:
        break
    else:
        print("lente of the passeword need to be more than 8 caractairs")

# chek if he use a patern 
start=time.time()
etat=False

with open("rockyou.txt","r", encoding="latin-1")as f:
    for i in f :
        if code == i.strip() :
            etat=True
            break

end=time.time()
print(f"Time taken: {end - start:.2f} seconds")

# chek if he have caractair and numebre and sumbole
if etat==False:
    print("no patern fund")
    charactair=False
    number=False
    sumbole=False
    strength=0
    for i in code :
        if i in string.ascii_letters and charactair==False:
            charactair=True
            strength=strength+1
        if i in string.digits and number==False:
            number=True
            strength=strength+1
        if i in string.punctuation and sumbole==False:
            sumbole=True
            strength=strength+1

    if strength == 1:
        print("bad")
    elif strength==2:
        print("normal")
    elif strength==3:
        print("exelent")
else:
    print("it is a coment pasword use another one")
# if note give hime a segtion with ia
# give hime the shose to aprov it or refusit 
# if he refeuset give hime a nother shose 
# if he aprovit give hime the shose to exite 