def decrypt(text, key):
    text = [char for char in text if char != ' ']
    rail = [['' for _ in text] for _ in range(key)]
    dir_down = row = col = 0

    for _ in text:
        if row in [0, key - 1]:
            dir_down = not dir_down
        rail[row][col] = '*'
        col += 1
        row += 1 if dir_down else -1

    index = 0
    for i in range(key):
        for j in range(len(text)):
            if rail[i][j] == '*' and index < len(text):
                rail[i][j] = text[index]
                index += 1

    string1 = []
    row = col = 0
    for _ in text:
        if row in [0, key-1]:
            dir_down = not dir_down
        if rail[row][col] != '*':
            string1.append(rail[row][col])
            col += 1
        row += 1 if dir_down else -1

    print("Decrypted message:\n", ''.join(string1))

decrypt('Horielteeredlhfn', 3)