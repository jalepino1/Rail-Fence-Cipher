from RailDecrypt import decrypt
from encrypt import encryptRailFence
import tkinter as tk
from tkinter .messagebox import *


def get_text_encrypt():
    global input_text
    inp = input_text.get(1.0, "end-1c") 
    key = key_text.get(1.0, "end-1c")
    input_text.delete(1.0, "end")  # Clear the input text widget
    input_text.insert(1.0, "encrypted message: ")
    input_text.insert("end", encryptRailFence(str(inp), int(key)))



def get_text_decrypt():
    global input_text
    inp = input_text.get(1.0, "end-1c") 
    key = key_text.get(1.0, "end-1c")
    input_text.delete(1.0, "end")  # Clear the input text widget
    input_text.insert(1.0, "decrypted message: ")
    input_text.insert("end", decrypt(str(inp),int(key)))




root = tk.Tk()
global input_text
input_text = tk.Text(root,height=4, width=50, font=('Comic-sans', 20))
key_text = tk.Text(root, height=1, width=20 ,font=('Comic-sans', 20))
key_text.grid(row=1, column=0, padx=20, pady=10, columnspan=2)
input_text.grid(row=0, column=0, padx=10, pady=5, columnspan=2)

key_label = tk.Label(root, text="Enter Key:", font=('Comic-sans', 16))
key_label.grid(row=1, column=0, padx=20, pady=10, sticky="w")

#key_text.insert(1.0, "*Replace with your key*")
input_text.insert(1.0, "*Replace with your Plaintext or Ciphertext*")
decrypt_button = tk.Button(root, text='Decrypt', command=get_text_decrypt, width=20, font=('Comic-sans', 20))
decrypt_button.grid(row=2, column=0, padx=(100, 0), pady=(20, 0))

encrypt_button = tk.Button(root, text="Encrypt", command=get_text_encrypt, width=20, font=('Comic-sans', 20))
encrypt_button.grid(row=2, column=1, padx=(0, 100), pady=(20, 0))

tk.Label(root, text="answer=").grid(row=4)
tk.Button(root, text='Show').grid(row=4, column=2, pady=4)




root.geometry("800x500")
root.title("Rail Fence Decryption and Encryption")

var = '12'
test = tk.Label(root, textvariable=var, width=20)


root.mainloop()


