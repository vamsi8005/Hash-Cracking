import hashlib
hash = input("enter a hash -> ")
passwords = ["admin","1234567890","123456","root","msfadmin","0987654321","098765","543210","112233","qazxcvbnm"]
length = len(hash)
if length == 32:
    print(f"Type {hash} -> MD5")
    for password in passwords:
        finall_hash = hashlib.md5(password.encode()).hexdigest()
        if hash == finall_hash:
            print(f" HASH {hash} -> was broken 💀💀💀💀 -> {password}")
            break
    else:
        print(f"Never give up bro......😤😤😤😤")
if length == 40:
    print(f"Type of {hash} -> SHA1")
    for password in passwords:
        finall_hash = hashlib.sha1(password.encode()).hexdigest()
        if hash == finall_hash:
            print(f" HASH {hash} -> was broken 💀💀💀-> {password}")
            break
    else:
        print(f"Never give up bro......😤😤😤😤")
if length == 64:
    print(f"Type of {hash} -> SHA256")
    for password in passwords:
        finall_hash = hashlib.sha256(password.encode()).hexdigest()
        if hash == finall_hash:
            print(f" HASH {hash} -> was broken💀💀💀-> {password} ")
            break
    else:
        print(f"Never give up bro......😤😤😤😤")
if length == 128:
    print(f"Type of {hash} -> SHA1")
    for password in passwords:
        finall_hash = hashlib.sha512(password.encode()).hexdigest()
        if hash == finall_hash:
            print(f" HASH {hash} -> was broken💀💀💀 -> {password} ")
            break
    else:
        print(f"Never give up bro......😤😤😤😤")

