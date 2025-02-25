import cv2
import os
import string

def encrypt_image(image_path, output_path, msg, password):
    img = cv2.imread(image_path)

    d = {chr(i): i for i in range(255)}

    m = 0
    n = 0
    z = 0

    for i in range(len(msg)):
        img[n, m, z] = d[msg[i]]
        n = n + 1
        m = m + 1
        z = (z + 1) % 3

    cv2.imwrite(output_path, img)
    os.system("start encryptedImage.png")
    print(f"Encrypted image saved as {output_path}")

if __name__ == "__main__":
    image_path = "E:/Users/Admin/Downloads/Stenography-main/Stenography-main/Photo.jpg"
    output_path = "encryptedImage.png"  
    
    msg = input("Enter secret message: ")
    password = input("Enter a password: ")

    encrypt_image(image_path, output_path, msg, password)
