from RailDecrypt import decrypt
from encrypt import encryptRailFence
import tkinter as tk



root = tk.Tk()




def get_text_encrypt():
    inp = input_text.get(1.0, "end-1c") 
    key = key_text.get(1.0, "end-1c")
    print(inp,"encrypt")
    print(key)
    encrypted = encryptRailFence(str(inp),int(key))
    return(encrypted)

def get_text_decrypt():
    inp = input_text.get(1.0, "end-1c") 
    key = key_text.get(1.0, "end-1c")
    print(inp,"decrypt")
    print(key)
    decrypt(str(inp),int(key))
    
               


input_text = tk.Text(root,height=4, width=50, font=('Comic-sans', 20))
key_text = tk.Text(root, height=1, width=20 ,font=('Comic-sans', 20))
key_text.grid(row=1, column=0, padx=20, pady=10, columnspan=2)
input_text.grid(row=0, column=0, padx=10, pady=5, columnspan=2)

key_label = tk.Label(root, text="Enter Key:", font=('Comic-sans', 16))
key_label.grid(row=1, column=0, padx=20, pady=10, sticky="w")

key_text.insert(1.0, "*Replace with your key*")
input_text.insert(1.0, "*Replace with your Plaintext or Ciphertext*")
decrypt_button = tk.Button(root, text='Decrypt', command=get_text_decrypt, width=20, font=('Comic-sans', 20))
decrypt_button.grid(row=2, column=0, padx=(100, 0), pady=(20, 0))

encrypt_button = tk.Button(root, text="Encrypt", command=get_text_encrypt, width=20, font=('Comic-sans', 20))
encrypt_button.grid(row=2, column=1, padx=(0, 100), pady=(20, 0))


output = tk.Text(root, height=1, width=20, font=("Comic-sans", 20))
output.grid(row=4, column=0)
output.insert(1.0, )
root.geometry("800x500")
root.title("Rail Fence Decryption and Encryption")



root.mainloop()


