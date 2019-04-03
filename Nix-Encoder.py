###Pre Req's###
#Need tkinter

#Use this code in anyway you want!

from tkinter import *
from tkinter.messagebox import *
alphabet = [' ','a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z','A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z','!','0','"','#','$','%','&','\',','()','.','*','+',',','-','.','/',':',';','<','=','>','?','@','[','\','] 

def primeNumbers(a,m):
    for i in range(2,m+1):
        if m % i == 0 and a % i == 0:
            return False
    return True

#This function will convert the first given keyword and convert it to a number 
def firstConvert(text):
    textList = []
    total = 0
    index = 0
    for i in range(len(text)):
    #Changes each letter in the given keyword to a number and combines them
        a = (ord(text[i]))
        textList.append(a)

    while index < len(textList):
        total = total + textList[index]
        index = index + 1
        total1 = total * total
    return total1

#This function will convert the second given keyword and convert it to a number       
def secondConvert(text):
    textList = []
    total = 0
    index = 0
    for i in range(len(text)):
    #Changes each letter in the given keyword to a number and combines them
        a = (ord(text[i]))
        textList.append(a)

    while index < len(textList):
        total = total + textList[index]
        index = index + 1
        total1 = total * total
    return total1

#This function will taken the number given from the conversion above
#This also calculates all of the prime numbers with the range of the Given Number to Given Number - 100, Example: Range between 10238 and 10138.
def calcPrime(givenNumber):
    lower = givenNumber - 100
    upper = givenNumber
    primeList = []
    for num in range(lower,upper + 1):
       # prime numbers are greater than 1
       if num > 1:
           for i in range(2,num):
               if (num % i) == 0:
                   break
           else:
                primeList.append(num)
    return primeList

#This fucntion takes all of the prime number produces in the function above and returns the highest prime number found 
def highestPrime(primeList):
    max = 0
    for i in primeList:
        if i > max:
            max=i
            max1 = max
    return max1

#Affine Cipher Encryption Code
def affine(a,b,m,plaintext):
    prime = primeNumbers(a,m)
    if prime == False:
        print("")
    else:
        ciphertext = ""
        for i in range(len(plaintext)):
            letter = plaintext[i]
            p = alphabet.index(letter)
            cipherNum = (a * p + b)% m 
            cipherLetter = alphabet[cipherNum]
            ciphertext = ciphertext + cipherLetter
        
        return ciphertext

#This is used for decrypting the cipher text
def inverse(a,m):
    x = 0
    for x in range(m):
        b = (a*x)%m
        if b == 1:
            return x
#Affine Cipher Decryption code
def decryptMessage(a,b,m,ciphertext):
    x = inverse(a,m)
    if inverse == '':
        print("")
    else:
        plaintext = ''
        for i in range(len(ciphertext)):
            letter = ciphertext[i]
            c = alphabet.index(letter)
            plainNum = (x * (c - b))% m
            plaintextLetter = alphabet[plainNum]
            if alphabet[plainNum] == 0:
                plaintext = plaintext + ' '
            else:
                
                plaintext = plaintext + plaintextLetter
            
        return plaintext

#Function that is set to the button to encrypt the message
def clickedEncryption():
    m=26
    text = num1.get()
    text2 = num2.get()
    s1 = firstConvert(text)
    s2 = secondConvert(text2)
    c1 = calcPrime(s1)
    c2 = calcPrime(s2)
    a = highestPrime(c1)
    a2 = highestPrime(c2)
    prime = primeNumbers(a,m)
    prime2 = primeNumbers(a2,m)
    plaintext = message.get()
    encryption = affine(a,a2,m,plaintext)
    r = Tk()
    r.withdraw()
    r.clipboard_clear()
    r.clipboard_append(encryption)
    r.update() 
    r.destroy()
    encrypt.insert(0,encryption)


#Function that is set to the button to decrypt the message
def clickedDecryption():
    m=26
    text = num1.get()
    text2 = num2.get()
    s1 = firstConvert(text)
    s2 = secondConvert(text2)
    c1 = calcPrime(s1)
    c2 = calcPrime(s2)
    a = highestPrime(c1)
    a2 = highestPrime(c2)
    prime = primeNumbers(a,m)
    prime2 = primeNumbers(a2,m)
    ciphertext = message.get()
    decryption = decryptMessage(a,a2,m,ciphertext)
    r = Tk()
    r.withdraw()
    r.clipboard_clear()
    r.clipboard_append(decryption)
    r.update() # now it stays on the clipboard after the window is closed
    r.destroy()
    decrypt.insert(0,decryption)
    


#Very simple tkinter UI to display the encrypted and decrypted outputs
main = Tk()
main.title("NDKrpyt")
main.geometry('250x135')
main.configure(bg="blue")
Label(main, text = "Keyword 1:", bg='lightblue').grid(row=0)
Label(main, text = "Keyword 2:",bg='lightblue').grid(row=1)
Label(main, text = "  Message: ",bg='lightblue').grid(row=2,column=0)
Label(main, text = "Decryption:").grid(row=3,column=1)


num1 = Entry(main)
num2 = Entry(main)
message = Entry(main)
encrypt = Entry(main)
decrypt = Entry(main)


num1.grid(row=0, column=1)
num2.grid(row=1, column=1)
message.grid(row=2, column=1)
encrypt.grid(row=4, column=0)
decrypt.grid(row=4, column=1)

Button(main, bg="lightgreen", fg="black", text='Encryption', command=clickedEncryption).grid(row=3, column=0, pady=4)
Button(main, bg="lightgreen", fg="black", text='Decryption', command=clickedDecryption).grid(row=3, column=1, pady=4)

mainloop()
