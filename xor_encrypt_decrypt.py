import tkinter as tk
from tkinter import ttk


def xor_encrypt_decrypt(text, key):
   
    key = key.encode('utf-8')
    key_length = len(key)
    
   
    text_bytes = text.encode('utf-8')
    result = bytearray()

    
    for i in range(len(text_bytes)):
        result.append(text_bytes[i] ^ key[i % key_length])
    
    
    try:
        return result.decode('utf-8')
    except UnicodeDecodeError:
      
        return result.decode('utf-8', errors='replace')


def encrypt():
    try:
        key = key_entry.get()
        text = text_input.get("1.0", tk.END).strip()
        encrypted_text = xor_encrypt_decrypt(text, key)
        result_output.config(state=tk.NORMAL)
        result_output.delete("1.0", tk.END)
        result_output.insert(tk.END, encrypted_text)
        result_output.config(state=tk.DISABLED)
    except Exception as e:
        result_output.config(state=tk.NORMAL)
        result_output.delete("1.0", tk.END)
        result_output.insert(tk.END, f"Error: {e}")
        result_output.config(state=tk.DISABLED)


def decrypt():
    try:
        key = key_entry.get()
        text = text_input.get("1.0", tk.END).strip()
        decrypted_text = xor_encrypt_decrypt(text, key)
        result_output.config(state=tk.NORMAL)
        result_output.delete("1.0", tk.END)
        result_output.insert(tk.END, decrypted_text)
        result_output.config(state=tk.DISABLED)
    except Exception as e:
        result_output.config(state=tk.NORMAL)
        result_output.delete("1.0", tk.END)
        result_output.insert(tk.END, f"Error: {e}")
        result_output.config(state=tk.DISABLED)


root = tk.Tk()
root.title("XOR Encryption/Decryption")


tk.Label(root, text="Key:").grid(row=0, column=0, padx=10, pady=10)
key_entry = tk.Entry(root, width=30)
key_entry.grid(row=0, column=1, padx=10, pady=10)

tk.Label(root, text="Text:").grid(row=1, column=0, padx=10, pady=10)
text_input = tk.Text(root, height=10, width=50)
text_input.grid(row=1, column=1, padx=10, pady=10)

tk.Button(root, text="Encrypt", command=encrypt).grid(row=2, column=0, padx=10, pady=10)
tk.Button(root, text="Decrypt", command=decrypt).grid(row=2, column=1, padx=10, pady=10)

tk.Label(root, text="Result:").grid(row=3, column=0, padx=10, pady=10)
result_output = tk.Text(root, height=10, width=50, state=tk.DISABLED)
result_output.grid(row=3, column=1, padx=10, pady=10)


root.mainloop()

#Encryption: Enter some text and a key, then click "Encrypt." 
# Verify that the encrypted output is gibberish.
#decryption: Take the encrypted text from second textbox and put it in first textbox and use the same key to decrypt it. 
# The result should be the original text.