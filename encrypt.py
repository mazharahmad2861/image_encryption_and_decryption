import numpy as np
from PIL import Image

# Logistic map function
def logistic_map(x, r):
    return r * x * (1 - x)

# Generate chaotic key using logistic map
def generate_chaotic_key(length, image_size, x0, r):
    key = []
    x = x0
    for _ in range(length):
        x = logistic_map(x, r)
        key.append(x)
    return (np.array(key).reshape([image_size[1], image_size[0], 4]) * 255).astype(np.uint8)
    
    
# Encryption function
def encrypt_image(image_path, key):
    # Open the image
    img = Image.open(image_path)
    img_array = np.array(img).astype(np.uint8)
    print(img_array.shape)
    # Perform encryption using XOR operation
    encrypted_data = np.bitwise_xor(img_array, key)

    # Create encrypted image from encrypted data
    encrypted_img = Image.fromarray(encrypted_data)
    return encrypted_img

# Decryption function
def decrypt_image(encrypted_img_path, key):
    # Open the encrypted image
    encrypted_img = Image.open(encrypted_img_path)
    encrypted_array = np.array(encrypted_img)

    # Perform decryption using XOR operation
    decrypted_data = np.bitwise_xor(encrypted_array, key)

    # Create decrypted image from decrypted data
    decrypted_img = Image.fromarray(decrypted_data.astype(np.uint8))
    return decrypted_img

# Example usage
if __name__ == "__main__":
    # Parameters
    image_path = "nainital.png"
    encrypted_image_path = "encrypted_image.png"
    decrypted_image_path = "decrypted_image.png"
    image_size = (1200, 800)  
    key_length = image_size[0] * image_size[1] * 4

    # Logistic map parameters
    x0 = 0.1  # Initial condition
    r = 3.9  # Parameter for logistic map

    # Generate chaotic key
    chaotic_key = generate_chaotic_key(key_length, image_size, x0, r)
    print(chaotic_key)
    # Encrypt the image
    encrypted_img = encrypt_image(image_path, chaotic_key)
    # print(encrypted_img)
    encrypted_img.save(encrypted_image_path)

    # Decrypt the image
    decrypted_img = decrypt_image(encrypted_image_path, chaotic_key)
    decrypted_img.save(decrypted_image_path)