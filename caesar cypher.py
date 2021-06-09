import string
import collections
import sys
#Importing necessary functions
CipherMode = input("Would you like to Encrypt or Decrypt yor message?")
def Solver(OriginalMessage, RotationValue):
    # Here I've defined my multi arguement function to encrypt and by how much to rotate the alphabet by
    upper = collections.deque(string.ascii_uppercase)
    lower = collections.deque(string.ascii_lowercase)
    # These are 2 deques which store the upper and lowercase values of the alphabet and their corresponding ascii value
    upper.rotate(RotationValue)
    lower.rotate(RotationValue)
    # this shows how much each deque is rotated by and it's  decided by the Rotation value we give it
    upper = ''.join(list(upper))
    lower = ''.join(list(lower))
    # Here we join the lists together to allow us to use the maketrans function
    return OriginalMessage.translate(str.maketrans(string.ascii_uppercase, upper)).translate(str.maketrans(string.ascii_lowercase, lower))

def AutoDecryption(CommonWords):
   for i in range(len(string.ascii_uppercase)):
       print(i, Solver(OriginalMessage))
#this decrypts in file for full range of uppercase letters
def AutoDecrypt2(Check):
    global text,CommonWords #taken from outside function
    EngDictionary = open(r'C:\Users\ilias\Documents\english-dictionary-500.txt', "r")
    EngDictionary.readlines()#
    AutoMessage=0
    FinalMessage= []
    DictionaryList=[]#2 lists to store values we find in matches
    for obj in EngDictionary:
        WordDictionary=str("".join(list(obj.split())))
        DictionaryList.append(WordDictionary)#any values are added to dictionary
    while AutoMessage< len(text):
        for item in range(len(string.ascii_uppercase)):
            SimilarWord= Solver(text,item).split()#turning decrypted value to a list
            Similar=list(set(DictionaryList).intersection(SimilarWord))#the intersection between the the decrypted message and dictionary
            if len(Similar)>1:
                print(AutoMessage)
                AutoDecryption(AutoMessage,item)
                Finish=input("Is this the correct value")
                if Finish=="yes":
                    print("Message has a rotation of", item)#the rotation value and the item is in range of length of list
                    AutoMessage+=1
                    FinalMessage.append(text)
                    break
    ActualFinalMessage=''.join(FinalMessage)#join list together
    print("The final message is"+ActualFinalMessage.upper())
    Analysis(ActualFinalMessage)

def Analysis(Message):
    Message.lower()
    WordCounter = Message.split()
    Uniq=set(WordCounter)#removes duplicates

    from collections import Counter
    print("There are", len(Uniq) ,"unique words")

    print("There are", len(WordCounter), "words")#length of total words

    q=(Counter(Message.split()))
    sorted(q)
    print(q.most_common(10))#10 most common words


    print("The most common letter is", collections.Counter(Message).most_common(1)[0])
    MinLength=len(min(WordCounter, key=len))
    MaxLength=len(max(WordCounter,key=len))#max and min length using length order
    print("The longest word is",MaxLength,"letters long")
    print("The shortest word length is", MinLength, "letters long")
    average = int(sum(len(word) for word in WordCounter) / len(WordCounter))
    print("The average word length is", average, "to the nearest whole number")


    # function to decrypt automatically

if CipherMode.lower() == "encrypt":
    print("Encryption selected!")
    while True:
        try:
            RotVal = int(input("By what value would you like to rotate by?"))
            break
        except ValueError:
            print("Integer, please.")

#try and except to avoid error message

elif "decrypt" == CipherMode.lower():
    print("Decryption selected!")

else:
    print("This isn't a valid input. Try again with 'encrypt' or 'decrypt'!")
    sys.exit(0)

TypeChoice = input("Would you like to use a message or file? Please print one.")
if TypeChoice.lower() == "file":

# Open the file with read only permit
    while True:
            FileName = input("What's the filename?")
            try:
                f = open(FileName, "r")
            except FileNotFoundError:
                print("Try a valid file name")
            else:
                break
# use read to read all lines in the file
    text = f.read()
# close the file after reading the lines.
    f.close()
elif TypeChoice.lower() == "message":
    OriginalMessage = input("Press enter to start.")
    print("When you've finished your message press enter to the question with no input")
    TotalLines = []
    while True:
        line = input("What's your Message?")
        print("When you've finished your message press enter to the question with no input")
        if line:
            TotalLines.append(line)
        else:
            break
    text = str('\n'.join(TotalLines))
else:
    print("Try again and restart the program, print 'message' or 'file' only")
    sys.exit(0)

if CipherMode.lower() == "encrypt":
    # function to encrypt
    print((Solver(text, RotVal)).upper())
    # Message to show that answer has been displayed
    Analysis(text)






if CipherMode.lower() == "decrypt" and TypeChoice.lower() == "message":
    DecryptionType = input("Would you like to choose a rotation value or automatically decrypt?. Print 'auto' or 'rotate'")
    while DecryptionType.lower() != "rotate" or "auto": #gives options of what to choose
        if DecryptionType.lower() == "rotate":
            while True:
                try:
                    RotValue = int(input("By what value would you like to rotate by?"))
                    break
                except ValueError:
                    print("Integer, please.")#only allows integers
            Test= 26-RotValue
            print(Solver(text, RotValue).upper())
            Analysis(text)
            break
        elif DecryptionType.lower() == "auto":
            AutoDecrypt2(OriginalMessage)
            Analysis(f)
        else:
            DecryptionType#prints input again

if CipherMode.lower() == "decrypt" and TypeChoice.lower() == "file":
    DecryptionType = input("Would you like to choose a rotation value or automatically decrypt?. Print 'auto' or 'rotate'")

    if DecryptionType.lower() == "rotate":
            while True:
                try:
                    RotValue = int(input("The original rotation?"))
                    break
                except ValueError:
                    print("Integer, please.")
            Test2 = RotValue
            print( Solver(text, Test2).upper())
            Analysis(text)
    elif DecryptionType.lower() == "auto":
            AutoDecrypt2(text)
            Analysis(text)
    else:
            print("Please use a valid input")
            DecryptionType#repeats asking about input



