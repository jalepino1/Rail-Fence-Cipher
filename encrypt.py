def encryptRailFence(text, key):
    # Convert the input text to a list of characters, excluding spaces
    text = list(''.join([char for char in text if char != ' ']))
    
    # Create a matrix (rail fence) with 'key' number of rows and length of text columns
    rail = [['' for i in range(len(text))] for j in range(key)]
    print(text)

    # Initialize direction (downward) and starting position (first row, first column)
    dir_down = False
    row, col = 0, 0
    
    # Iterate through each character in the text
    for i in range(len(text)):
        # Toggle direction if at the first or last row
        if (row == 0) or (row == key - 1):
            dir_down = not dir_down
         
        # Place the character in the matrix
        rail[row][col] = text[i]
        col += 1
        if dir_down:
            row += 1
        else:
            row -= 1
    
    # Construct the encrypted string by concatenating characters from each row
    string1 = ''
    for j in range(key):
        for x in rail[j]:
            string1 += '' + x
<<<<<<< HEAD
    
    # Return the final encrypted string
    return (string1)
=======
                 
    return(string1)


print(encryptRailFence("hello tehre friend", 2))

>>>>>>> 308e5b6 (Rail fence cipher finished)
