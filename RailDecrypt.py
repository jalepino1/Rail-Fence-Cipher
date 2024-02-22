
def decrypt(text, key):
    # take out spaces inside the text
    text = list(''.join([char for char in text if char != ' ']))
    # intialize the matrix to the length of text, and value of key
    rail = [['' for i in range(len(text))] for j in range(key)] 

    # set dir_down to initalize where the algorithm starts placing characters
    dir_down = None
    row, col = 0, 0
     
    # iterate through the length of text
    for i in range(len(text)):
        # whenever we reach key k::-1 we change the directtion to go up
        if row == 0 or row == key - 1:
            dir_down = not dir_down
        # place a * at the designated row and column in the matrix rail  
        rail[row][col] = '*a'
        col += 1
        if dir_down:
            row += 1
        else:
            row -= 1
    
    index = 0
    # iterate through the range of key
    for i in range(key):
        # iterate through the range of length text
        for j in range(len(text)):
            # if the selected row and column in the matrix rail is '*a' and index is less than length of text
            if ((rail[i][j] == '*a') and (index < len(text))):
                # append the value of index inside text
                rail[i][j] = text[index]
                # increase index by 1
                index += 1

    string1 = []
    row, col = 0, 0
    
    #iterate through the length of list
    for i in range(len(text)):
         
        if (row == 0):
            dir_down = True
        if (row == key-1):
            dir_down = False

        # if the character at rail[row][col] is not a '*' it appends the value into string1
        if (rail[row][col] != '*a') :
            string1.append(rail[row][col])
            col += 1
         
        if dir_down:
            row += 1
        else:
            row -= 1

    #return the string         
    return(string1)
