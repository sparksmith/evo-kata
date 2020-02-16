def readFile(fileLocation):
    print("--> Reading file: ",fileLocation)
    file = open(fileLocation, "r", encoding="utf-8")
    return file.read()

def writeResult(fileLocation, text):
    print("--> Writing to file: ",fileLocation)
    file = open(fileLocation, "w", encoding="utf-8")
    file.write(text)
    file.close()