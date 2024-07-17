from PIL import Image
import numpy as np

def encrypt_image(image_path, key):
    try:
        # Opening the image
        original_image = Image.open(image_path)
    except FileNotFoundError:
        print("Error: Image file not found.")
        return
    except Exception as e:
        print(f"Error: {e}")
        return

    # Converting the image to a NumPy array
    image_array = np.array(original_image)

    # Applying XOR operation with the key for encryption
    encrypted_image_array = image_array ^ key

    # Creating a new image from the encrypted NumPy array
    encrypted_image = Image.fromarray(np.uint8(encrypted_image_array))

    # Saving the encrypted image
    encrypted_image_path = "encrypted_image.png"
    encrypted_image.save(encrypted_image_path)
    print(f"Image encrypted successfully. Encrypted image saved at: {encrypted_image_path}")

def decrypt_image(encrypted_image_path, key):
    try:
        # Opening the encrypted image
        encrypted_image = Image.open(encrypted_image_path)
    except FileNotFoundError:
        print("Error: Encrypted image file not found.")
        return
    except Exception as e:
        print(f"Error: {e}")
        return

    # Converting the image to a NumPy array
    encrypted_image_array = np.array(encrypted_image)

    # Applying XOR operation with the key for decryption
    decrypted_image_array = encrypted_image_array ^ key

    # Creating a new image from the decrypted NumPy array
    decrypted_image = Image.fromarray(np.uint8(decrypted_image_array))

    # Saving the decrypted image
    decrypted_image_path = "decrypted_image.png"
    decrypted_image.save(decrypted_image_path)
    print(f"Image decrypted successfully. Decrypted image saved at: {decrypted_image_path}")

def main():
    while True:
        print("------------- Image Encryption Tool --------------")
        print("Select an option:")
        print("e - Encrypt image")
        print("d - Decrypt image")
        print("q - Quit")
        choice = input("Your choice: ").strip().lower()

        if choice == 'e':
            encrypt_choice()
        elif choice == 'd':
            decrypt_choice()
        elif choice == 'q':
            print("Exiting the program.")
            break
        else:
            print("Invalid choice. Please choose 'e' for encryption, 'd' for decryption, or 'q' to quit.")

def encrypt_choice():
    while True:
        try:
            key = int(input("Enter encryption key (0-255): "))
            if 0 <= key <= 255:
                break
            else:
                print("Invalid key. Please enter a number between 0 and 255.")
        except ValueError:
            print("Invalid input. Please enter a valid number.")

    image_location = input("Enter the location of the image: ").strip()
    encrypt_image(image_location, key)

def decrypt_choice():
    while True:
        try:
            key = int(input("Enter decryption key (0-255): "))
            if 0 <= key <= 255:
                break
            else:
                print("Invalid key. Please enter a number between 0 and 255.")
        except ValueError:
            print("Invalid input. Please enter a valid number.")

    encrypted_image_location = input("Enter the location of the encrypted image: ").strip()
    decrypt_image(encrypted_image_location, key)

if __name__ == "__main__":
    main()
