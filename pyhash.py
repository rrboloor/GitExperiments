import hashlib

def hashFromString(s):
    length=len(s)
    header="blob "+ str(length)+ '\0'
    print(header)
    store=header+s
    print(store)
    sha1=hashlib.sha1()
    sha1.update(store.encode('utf-8'))
    return sha1.hexdigest()

print(hashFromString("what is up, doc?\n"))
