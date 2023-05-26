import os
from cryptography.fernet import Fernet as Fernet

print("-"*100)
print("Disclaimer! - Keep The Files That You Want To Encrypt In The Same Folder As The App\nDo Not Delete/Modify/Rename The Do Not Delete.txt File\nKeep The Key File Save Without It You Wont Be Able To Decrypt Your Files")
print("-"*100)

def encrypt():
    global enc, Key
    
    if enc:
        print("Files are already encrypted.")
        choice()
    else:
        Key = Fernet.generate_key()
        with open("Key.key", "wb") as KeyFile:
            KeyFile.write(Key)
        
        for file in files:
            with open(file, "rb") as F:
                data = F.read()
                encryptData = Fernet(Key).encrypt(data)
            with open(file, "wb") as F:
                F.write(encryptData)
        
        print("Your files have been encrypted. Please keep the key file safe.")
        with open("!Do Not Delete.txt", "w") as check:
            check.write("VoiD")
        enc = True
        choice()

def decrypt():
    global enc, Key
    
    if not enc:
        print("Files are already decrypted.")
        choice()
    else:
        try:
            with open("Key.key", "rb") as KeyFile:
                Key = KeyFile.read()
            
            for file in files:
                with open(file, "rb") as f:
                    data = f.read()
                    DecryptData = Fernet(Key).decrypt(data)
                with open(file, "wb") as f:
                    f.write(DecryptData)
            
            print("Your files have been decrypted.")
            with open("!Do Not Delete.txt", "w") as check:
                check.write("Alien")
            enc = False
            choice()
        
        except:
            print("Key file not found or modified. Restart the app and try again.")
            choice()

def choice():
    while True:
        choice = input("\nEnter 1 to encrypt files, 2 to decrypt files, or 3 to exit: ")
        if choice == "1":
            encrypt()
            break
        elif choice == "2":
            decrypt()
            break
        elif choice == "3":
            break
        else:
            print("Error: Invalid input. Please try again.")


enc = None
files= []
for file in os.listdir():
    if file in ["Encrypt.py", "Decrypt.py", "!Do Not Delete.txt", "Key.key"]:
        continue
    else:
        files.append(file)

with open("!Do Not Delete.txt","r") as check:
    d = check.read()

if "Alien" in d:
    enc = False
elif "VoiD" in d:
    enc = True
else:
    print("Error: You have modified the do not delete file.")

choice()
