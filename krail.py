
    
def encryptRailFence(text, key):
  
    text = list(''.join([char for char in text if char != ' ']))
    print(text)
    rail = [
        ['' for i in range(len(text))] 
        for j in range(key)]
    
    print(rail)
    dir_down = False
    row, col = 0, 0
     
    for i in range(len(text)):
        if (row == 0) or (row == key - 1):
            dir_down = not dir_down
         
        rail[row][col] = text[i]
        col += 1
        if dir_down:
            row += 1
        else:
            row -= 1
    print(rail)
    result = []
    for i in range(key):
        for j in range(len(text)):
            if rail[i][j] != '\n':
                result.append(rail[i][j])
                #print(rail[i][j])
                
    return("" . join(result))

def start():

    choice = input("would you like to encrypt or decrypt a message?\n")
    if choice == "encrypt":
        key = input("Please insert a key that is >= 2:\n")
        key = int(key)
        if key >= 2:
            text = input('Please insert the message you would like to send\n:')
            print(encryptRailFence(text,key))
        else:
            print('INVALID Key')
            start()
    elif choice == "decrypt":
        dkey = input("what is your key?\n")
        dkey = int(dkey)
    else:
        print('That is not a valid answer, please select encrypt, or decrypt')
        start()

start() 

    

