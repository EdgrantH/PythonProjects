import time
import random

bannedChar = [":", ";", "<", ">", "^", "~", "[", "]", "{", "}", "`", "|", "\\"]

def check_if_banned(bannedChar, char):
    for i in bannedChar:
        if (i == char): 
            return True;
    
    return False 

def generate_password(length: int):
    str = ""
    for i in range(length):
        randAsc = random.randint(33, 126)
        newChar = chr(randAsc)

        while(check_if_banned(bannedChar, newChar)):
            randAsc = random.randint(33, 126)
            newChar = chr(randAsc)

        str += newChar

    return str


#main
#---------------------------------------------------------------------------------------------
print("Generating new password", end= "")

#loading animation
for i in range(3):
    print('.', end="")
    time.sleep(0.5)
print()

print("Your new password is: %s" % generate_password(20))