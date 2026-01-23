# Check whether a character is a vowel or consonant.

char = input("Enter a char : ")
Vowel = "aeiouAEIOU"
flag = False

for i in Vowel:
    if (char == i):
        flag = True
    
if (flag==True):
    print(char,"VOWEL")
else:
    print(char,"CONSONANT")

    


