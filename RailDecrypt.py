def decrypt(text, key):
    text = list(''.join([char for char in text if char != ' ']))
    rail = [['' for i in range(len(text))] for j in range(key)] 

    dir_down = None
    row, col = 0, 0
     
    for i in range(len(text)):
        if row == 0 or row == key - 1:
            dir_down = not dir_down
        rail[row][col] = '*'
        col += 1
        if dir_down:
            row += 1
        else:
            row -= 1


    index = 0
    for i in range(key):
        for j in range(len(text)):
            if ((rail[i][j] == '*') and
               (index < len(text))):
                rail[i][j] = text[index]
                index += 1

        string1 = []
    row, col = 0, 0
    for i in range(len(text)):
         
        if (row == 0):
            dir_down = True
        if (row == key-1):
            dir_down = False
             
        if (rail[row][col] != '*'):
            string1.append(rail[row][col])
            col += 1
         
        if dir_down:
            row += 1
        else:
            row -= 1

                 
    return(print("Decrypted message:\n",string1))

decrypt('Horielteeredlhfn', 3)