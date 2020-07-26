import sys

class encryptor:
    
    def __init__(self):
        pass
    
#    Enter your signature or any string (without spaces) for default key.
    def encrypt(self,msg,encryption,key="YOURSIGNATURE"):
        enMsg = ""
        if encryption == "CAESER":
            enMsg = self.caeser(msg,key)
        elif encryption == "VIGENERE":
            enMsg = self.vigenere(msg,key)
        return enMsg

#     Caesar Cipher
#     Each alphabet in message is replaced with other alphabets which occur after fixed no. of 
#     'step' in Alphabet series
#     When step = 3,
#     Original Alphabet series:    A B C D E F G H I J K L M N O P Q R S T U V W X Y Z
#     Replaced Alphabet series:    D E F G H I J K L M N O P Q R S T U V W X Y Z A B C
#     
#     For Example:
#     step = 3
#     Plain Text message is "HELLO EVERYONE"
#     cipher Text is "KHOOR HYHUBRQH"
    def caeser(self,msg,step):
        encrypted = ""
        if step.isnumeric():
            step = int(step)
        else:
            step = 5
        for ch in msg:
            if ch == ' ':
                encrypted += ch
            else:
                chAscii = ord(ch)+step
                if ord(ch)<=90 and chAscii > 90:
                    chAscii = 64+(chAscii%90)
                elif chAscii > 122:
                    chAscii = 96+(chAscii%122)
                encrypted += chr(chAscii)
        return encrypted

# Vigenere Table mapping wrt to key to encrypt message.
# Table composed of Alphabets written in sequential order. Each row has its alphabets shifted to left by one place relative to the above row.
#
#        | A B C D E F G H I J K L M N O P Q R S T U V W X Y Z
#     ___|_____________________________________________________
#      A | A B C D E F G H I J K L M N O P Q R S T U V W X Y Z
#      B | B C D E F G H I J K L M N O P Q R S T U V W X Y Z A
#      C | C D E F G H I J K L M N O P Q R S T U V W X Y Z A B
#      D | D E F G H I J K L M N O P Q R S T U V W X Y Z A B C
#      - | - - - - - - - - - - - - - - - - - - - - - - - - - -
#      - | - - - - - - - - - - - - - - - - - - - - - - - - - -
#      - | - - - - - - - - - - - - - - - - - - - - - - - - - -
#      Y | Y Z A B C D E F G H I J K L M N O P Q R S T U V W X
#      Z | Z A B C D E F G H I J K L M N O P Q R S T U V W X Y
#
#    Intersecting of chars from message and key is selected as the mapping of that messages's char
#    Each row char index is for message's char
#    Each column char index is for key's char

    def prepareTable(self):
        table = {}
        for i in range(65,91):
            li = []
            for j in range(i,91):
                li.append(chr(j))
                
            for j in range(65,i):
                li.append(chr(j))
            table.__setitem__(chr(i), li)
        return table
    
    def vigenere(self, msg, key):
        vTable = self.prepareTable()
        encrypted = ""
        for i in range(len(msg)):
            if msg[i] == ' ':
                encrypted+=" "
            else:
                replaceFrom = vTable[msg[i]]
                temp = vTable['A']
                encrypted += replaceFrom[temp.index(key[i%len(key)])]
        return encrypted
#
#------------------------------
#
class decryptor:
    
    def __init__(self):
        pass
    
    def decrypt(self,msg,encryptionType,key="YOURSIGNATURE"):
        message = ""
        if encryptionType == "CAESER":
            message = self.deCaeser(msg,key)
        elif encryptionType == "VIGENERE":
            message = self.deVigenere(msg,key)            
        return message
        
    def deCaeser(self,msg,step):
        decrypted = ""
        if step.isnumeric():
            step = int(step)
        else:
            step = 5
        for ch in msg:
            if ch == ' ':
                decrypted += ch
            else:
                chAscii = ord(ch)-step
                if chAscii < 65:
                    chAscii = 91-(65-chAscii)
                elif chAscii > 90 and chAscii < 97:
                    chAscii = 123-(97-chAscii)
                decrypted += chr(chAscii)
        return decrypted

# Vigenere Table mapping wrt to key to encrypt message.
# Table composed of Alphabets written in sequential order. Each row has its alphabets shifted to left by one place relative to the above row.
#    A B C D E F G H I J K L M N O P Q R S T U V W X Y Z
#    B C D E F G H I J K L M N O P Q R S T U V W X Y Z A
#    C D E F G H I J K L M N O P Q R S T U V W X Y Z A B
#    D E F G H I J K L M N O P Q R S T U V W X Y Z A B C
#    - - - - - - - - - - - - - - - - - - - - - - - - - -
#    - - - - - - - - - - - - - - - - - - - - - - - - - -
#    - - - - - - - - - - - - - - - - - - - - - - - - - -
#    Y Z A B C D E F G H I J K L M N O P Q R S T U V W X
#    Z A B C D E F G H I J K L M N O P Q R S T U V W X Y

    def prepareTable(self):
        table = {}
        for i in range(65,91):
            li = []
            for j in range(i,91):
                li.append(chr(j))
                
            for j in range(65,i):
                li.append(chr(j))
            table.__setitem__(chr(i), li)
            
        return table
         
    def deVigenere(self, msg, key):
        vTable = self.prepareTable()           
        decrypted = ""
        for i in range(len(msg)):
            if msg[i] == ' ':
                decrypted+=" "
            else:
                replaceFrom = vTable[msg[i]]
                temp = vTable['A']
                if key[i%len(key)] == 'A':
                    key2 = key[i%len(key)]
                else:
                    key2 = chr(65+91-ord(key[i%len(key)]))
                decrypted += replaceFrom[temp.index(key2)]
        return decrypted


# print('Number of arguments:', len(sys.argv), 'arguments.')
# print('Argument List:', str(sys.argv))
args = sys.argv
if args[1]:
    message = args[1].upper()
else:
    message = input("Enter your Message: ").upper()
    
if args[2]:
    encryptionType = args[2].upper()
else:
    encryptionType = "VIGENERE"
    
if encryptionType == 'VIGENERE':
    try:
        key = args[3].upper()
    except:
        pass
else:
    try:
        if args[3].isnumeric():
            key = args[3]
    except:
        key = ""

en = encryptor()
de = decryptor()
try:
    encrytpedMsg = en.encrypt(message,encryptionType, key)
    decryptedMsg = de.decrypt(encrytpedMsg, encryptionType, key)
except:
    encrytpedMsg = en.encrypt(message,encryptionType)
    decryptedMsg = de.decrypt(encrytpedMsg, encryptionType)
    
print(encrytpedMsg)
print(decryptedMsg)

print("...run complete...")