import cv2
import os
import string

def decrypt_image(image_path, password, msg_length):
    img = cv2.imread(image_path)

    
    c = {i: chr(i) for i in range(255)}

    message = ""
    n = 0
    m = 0
    z = 0

    pas = input("Enter passcode for Decryption: ")
    if password == pas:
        for i in range(msg_length):
            message = message + c[img[n, m, z]]
            n = n + 1
            m = m + 1
            z = (z + 1) % 3
        print("Decryption message:", message)
    else:
        print("YOU ARE NOT AUTHORIZED")

if __name__ == "__main__":
    image_path = "encryptedImage.png"  
    password = input("Enter the password used for encryption: ")
    msg_length = int(input("Enter the length of the secret message: "))

    decrypt_image(image_path, password, msg_length)
