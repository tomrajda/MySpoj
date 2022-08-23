import string

alphabet = list(string.ascii_uppercase)

while True:
    try:
        inpt = input()
        res = ""
        for letter in inpt:

            if letter == " ":
                res += letter
            else:

                if letter == "X":
                    res += "A"
                elif letter == "Y":
                    res += "B"
                elif letter == "Z":
                    res += "C"
                else:
                    
                    i = alphabet.index(letter)
                    n = alphabet[i+3]
                    res += n
        
        print(res)

    except EOFError:
        break

#https://pl.spoj.com/problems/JSZYCER/