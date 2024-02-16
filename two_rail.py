def two_rail(messsage):
    y = 0
    for x in range(len(messsage)):
        if messsage[x] != ' ':
            y+=1
    encrpyt = []
    encrpyt2 = []
    messsage = list(messsage)
    for x in messsage:
        if x == ' ':
            messsage.remove(x)
    for x in range(0, len(messsage), 2):
        encrpyt.append(messsage[x])
    for x in range(1, len(messsage), 2):
        encrpyt2.append(messsage[x])       
    encrpyt.extend(encrpyt2)
    string1 = ''
    for x in encrpyt:
        string1 += '' + x
    print(string1)
    return string1