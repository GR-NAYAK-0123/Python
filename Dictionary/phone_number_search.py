
# Finding mobile number from the register by the person's name

def search(names, register):
    result = []
    for i in names:
        if i in register:
            result.append(register[i])
        else:
            result.append("Not Found")
    return result


register = {}
register["sam"] = 99912222
register["tom"] = 11122222
register["harry"] = 12299933

names = ["sam", "caran", "harry"]

print("The result is :", search(names, register))