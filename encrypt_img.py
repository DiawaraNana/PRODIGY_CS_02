
from tkinter import Tk, Button, Label, filedialog, messagebox, Radiobutton, StringVar, Canvas, PhotoImage
from PIL import  Image, ImageTk
from datetime import datetime
import os
from cryptography.fernet import Fernet


if os.path.exists("key.key"):
    with open("key.key", "rb") as f:
        Key = f.read()
else:
    Key = Fernet.generate_key()
    with open("key.key", "wb") as f:
        f.write(Key)

fernet = Fernet(Key)



chemin = os.path.join(os.path.expanduser("~"), "Téléchargements/encrypt_decrypt_img")
os.makedirs(chemin, exist_ok=True)

def encrypt_img(image_data, chemin_image):
    encrypted_data = fernet.encrypt(image_data)
    with open(chemin_image, "wb") as f:
        f.write(encrypted_data)
    return chemin_image

def decrypt_img(image_data, chemin_image):
    decrypted_data = fernet.decrypt(image_data)
    with open(chemin_image, "wb") as f:
        f.write(decrypted_data)
    return chemin_image
    
class App:
   def __init__(self,root):
      self.root=root
      self.root.title("Image Encryption / Decryption Tool")
      self.root.config(background='#4B6DD2')
      self.root.geometry("720x480")
      self.label_title=Label(root,text="Image Encryption / Decryption Tool",font=("Helvetica",40),bg='#4B6DD2')
      self.label_title.pack(pady=10, padx=15)
      
      width=300
      height=250
      self.pil_image = Image.open("images.jpeg")
      self.image= ImageTk.PhotoImage(self.pil_image)
      self.canva=Canvas(root,width=width,height=height)
      self.canva.create_image(width/2,height/2,image=self.image)
      self.canva.pack(pady=20, padx=25)
      self.img_path=None
      
      self.action=StringVar(value='e')
      
      self.label = Label(root, text="No file selected")
      self.label.pack(pady=10)
      
      self.btn_select=Button(root,text="Select image",command=self.select_file,font=("Helvetica",15))
      self.btn_select.pack(pady=10)
      
      self.radio_encrypt=Radiobutton(root,text="Encrypt",variable=self.action,value='e',font=("Helvetica",15))
      self.radio_encrypt.pack(pady=10)
      
      self.radio_decrypt=Radiobutton(root,text="Decrypt",variable=self.action,value='d',font=("Helvetica",15))
      self.radio_decrypt.pack(pady=10)
      
      self.btn_run=Button(root,text="Run",command=self.run,font=("Times",25,"bold "),bg='white')
      self.btn_run.pack(pady=35)
      
   def select_file(self):
       path = filedialog.askopenfilename(
            title="Select an image file",
            filetypes=[("Image files", "*.png *.jpg *.jpeg *.bmp *.gif"), ("All files", "*.*")]
        )
       if path:
           self.img_path=path
           self.label.config(text=f"Selected: {os.path.basename(path)}")
           
       
   def run(self):
      if not self.img_path:
        messagebox.showerror("Error,image not selected!.")
        return
      if not os.path.isfile(self.img_path) :
        messagebox.showerror("Error, selected file doesn't exist!")
        return 

      with open(self.img_path, "rb") as f:
        image_data = f.read()

      choice = self.action.get()
      timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    
      extension = os.path.splitext(self.img_path)[1] or ".png"
      new_filename = f"image_{choice}_{timestamp}{extension}"
      output_path = os.path.join(chemin, new_filename)

      try:
        if choice == 'e':
            image_new = encrypt_img(image_data, output_path)
            messagebox.showinfo("Success", f"Image encrypted and saved at:\n{image_new}")
        else :
            image_new = decrypt_img(image_data, output_path)
            messagebox.showinfo("Success", f"Image decrypted and saved at:\n{image_new}")
     
       
        try:
            
            Image.open(image_new).show()
          
        except Exception:
            messagebox.showwarning("Warning", "Cannot open image automatically (maybe encrypted).")

      except Exception as e:
        messagebox.showerror(f"\nAn error occurred: {e}")

if __name__ == "__main__":
   root = Tk()
   app = App(root)
   root.mainloop()
  
