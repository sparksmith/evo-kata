def readFile(fileLocation):
    print("--> Reading file: ", fileLocation)
    result = ""
    with open(fileLocation, "r", encoding="utf-8") as file:
        result = file.read()

    return result


def writeResult(fileLocation, text):
    print("--> Writing to file: ", fileLocation)
    with open(fileLocation, "w", encoding="utf-8") as file:
        file.write(text)
