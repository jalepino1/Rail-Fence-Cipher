<<<<<<< HEAD
import tkinter

def encryptRailFence(text, key):
    #gui.Window(title="Hello World",layout=[[]], margins=(100, 100)).read()
=======

def encryptRailFence(text, key):
>>>>>>> abca330e1c1586b074950cb60a976ec4ce1f5650
    text = list(''.join([char for char in text if char != ' ']))
    rail = [['' for i in range(len(text))] for j in range(key)]

    dir_down = False
    row, col = 0, 0
     
    for i in range(len(text)):
        if (row == 0) or (row == key - 1):
            print(rail)
            dir_down = not dir_down
        rail[row][col] = text[i]
        col += 1
        if dir_down:
            row += 1
        else:
            row -= 1
    string1 = ''
    for j in range(key):
        for x in rail[j]:
            string1 += '' + x
                 
    return(print("Encrypted message:\n",string1))

<<<<<<< HEAD
def decryptRailFence(text,key):


    return
# Time complexity: O(N^2)
encryptRailFence('Hello there friend', 3)
=======
>>>>>>> abca330e1c1586b074950cb60a976ec4ce1f5650
