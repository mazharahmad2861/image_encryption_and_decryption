# Project Title: Image Encryption and Decryption Using Logistic Map

# Description:

This project implements a secure image encryption and decryption system using a chaotic logistic map. The logistic map is a mathematical function known for its unpredictable, chaotic behavior. It is used here to generate pseudo-random sequences that help in encrypting the pixel values of an image, ensuring security against unauthorized access.

### Features:

Chaos-based encryption using the logistic map

Symmetric key encryption and decryption

Supports both grayscale and RGB images

Basic statistical analysis like histogram and entropy

Protection against differential attacks

### How It Works:

The encryption is based on the logistic map equation:

xₙ₊₁ = r × xₙ × (1 − xₙ)



Where:

r is a control parameter (typically between 3.57 and 4.0 for chaotic behavior)

x₀ is the initial seed (this acts as the secret key)

#### Encryption steps:

Generate a chaotic sequence using the logistic map.

Shuffle or permute the image pixel positions based on the sequence.

Modify (diffuse) the pixel values using XOR with the generated sequence.

Save the resulting image as the encrypted image.

### Decryption steps:

Use the same x₀ and r values to regenerate the same chaotic sequence.

Reverse the pixel value modifications and pixel shuffling.

Reconstruct the original image.

### Parameters:

x₀: Initial value for the logistic map (should be between 0 and 1)

r: Control parameter (usually between 3.57 and 4.0 for chaotic behavior)

