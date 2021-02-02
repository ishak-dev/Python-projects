import random
length = 7
char = ("abcdefghijklmnoprstuvzxywq1234567890")

ok=True
while ok == True:
    passwordhash = [random.choice(char) for i in range(length)]
    password = "".join(passwordhash)
    print(password)
    r = input ("If you want to generate again press 'N' else press 'E': ")
    if(r=="n" or r == "N"):
        ok=True
    elif(r == "e" or r == "E"):
        ok=False
