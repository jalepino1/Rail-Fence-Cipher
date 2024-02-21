from RailDecrypt import decrypt
from encrypt import encryptRailFence
import tkinter as tk

root = tk.Tk()


root.geometry("800x500")
root.title("Rail Fence Decryption and Encryption")


textbox = tk.Text(root, height =6)
textbox.pack(padx=20,pady=20)


buttonframe = tk.Frame(root)
buttonframe.columnconfigure(0,weight=1)
buttonframe.columnconfigure(1,weight=1) 
decryption = tk.Button(buttonframe, text="Decrypt Text",font=('Comic-sans', 16))
decryption.grid(row=0,column=0, sticky=tk.W+tk.E)
encryption = tk.Button(buttonframe, text="Encrypt Text",font=('Comic-sans', 16))
encryption.grid(row=0,column=1,sticky=tk.W+tk.E)
buttonframe.pack(fill='x')



root.mainloop()


decrypt('tsigetn', 2)
encryptRailFence('testing',2)