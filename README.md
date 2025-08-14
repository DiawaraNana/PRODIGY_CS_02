# PRODIGY_CS_02
# Image Encryption and Decryption Tool

## Overview
This project is a **Tkinter-based application** that allows users to encrypt and decrypt images using the cryptography library’s **Fernet** symmetric encryption.
It was developed as part of my internship work.

Users can select an image file, apply encryption, and later decrypt it back to its original form. All operations are performed via an easy-to-use Graphical User Interface.

## Features
- Graphical Interface with Tkinter.

- Symmetric encryption using Fernet (AES + HMAC under the hood).

- Key persistence – the same key is reused for decryption if already generated.

- Simple workflow: Select → Encrypt → Decrypt.

This project was developed as part of my **internship** to demonstrate practical applications of Python for simple cryptographic operations.

---

##  Project Structure

project/
│
├── encrypt_img.py       # Main application file

├── key.key              # Encryption key (auto-generated if missing)

├── README.md            # Documentation

└── home/telechargements/encrypt_decrypt_img/   # Folder for encrypted/decrypted images

---

##  Requirements
Make sure you have **Python 3.x** installed and the required libraries:

```bash
pip install pillow
```
## Usage

> - Place Images

Store the image you want to encrypt in the folder:
home/kali/telechargements/encrypt_decrypt_img/
> - Run the Program
```bash
python encrypt_img.py
```
> - Follow the Menu

- Choose to encrypt or decrypt an image.
- Choose the image in the select section.
- Click on run to start.
  
> - Output

Images will be saved in the same folder with a name like:
- image_{choice}_{timestamp}{extension}
  
## How It Works

> - Encryption: The program reads the image pixel-by-pixel and applies mathematical transformations to change color values.

> - Decryption: The process is reversed to restore the original pixel values.

## Security Notes

Do not delete key.key if you want to decrypt previously encrypted images.

Fernet ensures AES encryption with authentication to prevent tampering.

- Encrypted images cannot be viewed normally in an image viewer.

- Always keep a copy of the original image, as incorrect parameters may make the image unrecoverable.
  
## Author

Developed by **DIAWARA NANA** during an internship project.
