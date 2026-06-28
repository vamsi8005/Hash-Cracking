#MD5 sha1 sha256 NTLm SHA 512
import hashlib 
Dumping_hash =input("enter a hashes:-")
clue_required = input("The hash u pasted here taken from  windows yes/no:--- ")
def Crack(Dumping_hash):
    found = False
    with open('/usr/share/wordlists/rockyou.txt','r', errors="ignore") as file:
        for password in file:
            passwords = password.strip()
            if len(Dumping_hash) == 32:
                if clue_required == "yes":
                    hashing =  hashlib.new('md4', passwords.encode('UTF-16LE')).hexdigest()
                    if  Dumping_hash == hashing:
                        print("hash Found...>>")
                        print(passwords)
                        found = True
                        break
                else:
                    hashing = hashlib.md5(passwords.encode()).hexdigest()
                    if  Dumping_hash == hashing:
                        print("hash Found...>>")
                        print(passwords)
                        found = True
                        break
            elif len(Dumping_hash) == 40:
                hashing = hashlib.sha1(passwords.encode()).hexdigest()
                if  Dumping_hash == hashing:
                        print("hash Found...>>")
                        print(passwords)
                        found = True
                        break
            elif len(Dumping_hash) == 64:
                hashing = hashlib.sha256(passwords.encode()).hexdigest()
                if  Dumping_hash == hashing:
                        print("hash Found...>>")
                        print(passwords)
                        found = True
                        break
            elif len(Dumping_hash) == 128:
                hashing = hashlib.sha512(passwords.encode()).hexdigest()
                if  Dumping_hash == hashing:
                        print("hash Found...>>")
                        print(passwords)
                        found = True
                        break
    if not found:
        print("HASH NOT FOUND")          
                
Crack(Dumping_hash)
