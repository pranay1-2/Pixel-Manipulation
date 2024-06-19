from PIL import Image
import numpy as np

def encrypt_decrypt_image(image_path, key, output_path, encrypt=True):
    # Open the image
    image = Image.open(image_path)
    image = image.convert("RGB")
    
    # Convert the image to a numpy array
    image_array = np.array(image)
    
    # Perform XOR operation with the key on each pixel
    key = int(key)
    if encrypt:
        encrypted_array = image_array ^ key
    else:
        encrypted_array = image_array ^ key
    
    # Convert the array back to an image
    encrypted_image = Image.fromarray(encrypted_array.astype('uint8'), 'RGB')
    
    # Save the encrypted/decrypted image
    encrypted_image.save(output_path)

def main():
    while True:
        choice = input("Do you want to (E)ncrypt or (D)ecrypt an image? (Enter 'Q' to quit): ").upper()
        if choice == 'Q':
            break
        if choice not in ['E', 'D']:
            print("Invalid choice. Please enter 'E' to encrypt, 'D' to decrypt, or 'Q' to quit.")
            continue

        image_path = input("Enter the path to the image file: ")
        key = input("Enter the encryption/decryption key (integer): ")
        output_path = input("Enter the path to save the output image: ")
        
        if choice == 'E':
            encrypt_decrypt_image(image_path, key, output_path, encrypt=True)
            print(f"Image encrypted and saved to {output_path}")
        else:
            encrypt_decrypt_image(image_path, key, output_path, encrypt=False)
            print(f"Image decrypted and saved to {output_path}")

if __name__ == "__main__":
    main()
