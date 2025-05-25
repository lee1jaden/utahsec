alphabet_length = 26

with open(r"cryptography/cipher/problem.txt", "r") as readFile:
    with open(r"cryptography/cipher/output.txt", "w") as writeFile:
        for line in readFile:
            writeFile.write("New line -------------------------------\n")
            encoded_words = line.split()
            #TODO: apply frequency analysis
            for i in range(alphabet_length):
                decoded_words = []
                for ew in encoded_words:
                    dw = ""
                    for letter in ew.upper():
                        letterIndex = (ord(letter) + i) % 26 + 65
                        dw = dw + chr(letterIndex)
                    decoded_words.append(dw)
                writeFile.write("Shift = {} | ".format(i))
                writeFile.write(" ".join(decoded_words) + "\n")
