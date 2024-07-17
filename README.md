# Prodigy_CS_02 - Image Encryption Tool

This project implements an image encryption tool using Python. It allows users to encrypt and decrypt images using pixel manipulation techniques and XOR operations.

## Features

- **Encryption**: Encrypt images using a provided key.
- **Decryption**: Decrypt images using the same key.
- **Pixel Manipulation**: Efficient pixel-level operations with NumPy.

## Installation

1. **Clone the repository**:
    ```bash
    git clone https://github.com/your-domzzy/Prodigy_CS_02.git
    cd Prodigy_CS_02
    ```

2. **Install dependencies**:
    ```bash
    pip install -r requirements.txt
    ```

## Usage

To use the image encryption tool, run the `image_encryption.py` script with the appropriate command-line arguments.

### Encrypt an Image

To encrypt an image, use the following command:
```bash
python image_encryption.py encrypt input_image.png encrypted_image.png 12345

    input_image.png: The path to the image you want to encrypt.
    encrypted_image.png: The path where the encrypted image will be saved.
    12345: The encryption key (replace with your desired key).

Decrypt an Image

To decrypt an image, use the following command:

bash

python image_encryption.py decrypt encrypted_image.png decrypted_image.png 12345

    encrypted_image.png: The path to the encrypted image.
    decrypted_image.png: The path where the decrypted image will be saved.
    12345: The encryption key (must be the same key used for encryption).

Example

Here's an example of how to use the tool:

bash

python image_encryption.py encrypt sample_input.png sample_encrypted.png 12345
python image_encryption.py decrypt sample_encrypted.png sample_decrypted.png 12345

License

This project is licensed under the MIT License. See the LICENSE file for details.

markdown


### Steps to Add README.md to Your Repository

1. **Navigate to Your Repository**:
   Go to your GitHub repository in your web browser.

2. **Add New File**:
   - Click the "Add file" button and select "Create new file".
   - Name the file `README.md`.

3. **Copy and Paste**:
   - Copy the content from the detailed `README.md` provided above.
   - Paste it into the newly created `README.md` file on GitHub.

4. **Commit the New File**:
   - Scroll to the bottom of the page.
   - Add a commit message (e.g., "Add detailed README.md").
   - Click "Commit new file".
