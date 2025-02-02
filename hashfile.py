# Python program to find the SHA-1 message digest of a file

import hashlib
def hash_file(filepath):
    h = hashlib.sha1()                    # make a hash object
    with open(filepath,"rb") as f1:     # open file for reading in binary mode
        chunk = 0
        while chunk != b"":
            chunk=f1.read(1024)         # read only 1024 bytes at a time
            h.update(chunk)
    return h.hexdigest()


# message=hash_file("")                    # Use path of the file
# print(message)