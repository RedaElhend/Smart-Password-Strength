# this just a code you will need to instal rockyou.txt to run it with this

import string
import time
from groq import Groq

client = Groq(api_key="api key of grop ;]")

def get_ai_suggestion(password):
    response = client.chat.completions.create(
        model="llama-3.1-8b-instant",
        messages=[
            {
                "role": "user",
                "content": f"My password is: {password}. Give me 1 stronger password that looks similar to it. Only give the password, nothing else."
            }
        ]
    )
    return response.choices[0].message.content

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
    if strength==3:
        print("it is a good pass word")
    else:
        chose = input("it is not a very secur pasword would you like a segetion for a better one? y/n :")
else:
    print("it is a coment pasword \n Suggested stronger password:", get_ai_suggestion(code))

while True:
    if chose == "y" or chose=="Y":
        print("Suggested stronger password:", get_ai_suggestion(code))
        break
    elif chose == "n" or chose=="N":
        print("havee a nice day")
        break
    else:
        print("you chose a invalide choise ")
        chose=input("would you like a segetion for a better one? y/n :")
