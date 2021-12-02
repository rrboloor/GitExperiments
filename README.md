# GitExperiments
Project created to learn git
## Git commit
## Git push
## Git fetch
## How git Calculates hash and simulation using python
To understand how git calculates hash of an object(blob). Lets simulate similar operation in Python and verify the git results.
Here is the tiny python function.
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
        
 ### Steps are:
   - Create a header with string starting "blob " (word blob and a space)
   - add length of the content in bytes
   - end the header with a null character
   - Concatenate header with content.
   - Generate hash function of header+content.

You can compare this result with git cli as 

 >  ' echo -n "whats is up,doc?" | git hash-object --stdin `
        
        
