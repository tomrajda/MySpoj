import string

strongs = []

for _ in range(int(input())):

    password = input()
    
    if len(password) >= 8:
        #Checking if the password has 
        # minimum 1 big letter
        if any(p in password for p in string.ascii_uppercase):
            #Checking if the password has 
            # minimum 1 low letter            
            if any(p in password for p in string.ascii_lowercase):
                #Checking if the password has 
                # minimum 1 digit                   
                if any(p in password for p in string.digits):
                    #Checking if the password has 
                    # minimum 1 punctuation                      
                    if any(p in password for p in string.punctuation):
                        strongs.append(password)
                    else:
                        continue
                else:
                    continue
            else:
                continue
        else:
            continue
    else:
        continue

for s in strongs:
    print(s)
                