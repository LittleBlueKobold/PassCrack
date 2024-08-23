import hashlib  #import hash library

def crack_password(hash_to_crack, wordlist_file):  #define crack function
    with open(wordlist_file, 'r') as file:  #uses designated wordlist
        for line in file:
            password = line.strip()
            hashed_password = hashlib.md5(password.encode()).hexdigest() #create password hash
            if hashed_password == hash_to_crack:
                return password
    return None

hash_to_crack = "5f4dcc3b5aa765d61d8327deb882cf99"  # md5 hash of password to crack
wordlist_file = "wordlist.txt"  #input desired wordlist here
print(f"Password: {crack_password(hash_to_crack, wordlist_file)}") #output