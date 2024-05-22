import random

# Function to check if a number is prime
def is_prime(num):
    if num < 2:
        return False
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            return False
    return True

# Function to check if a number is a primitive root modulo p
def is_primitive_root(g, p):
    if not is_prime(p):
        return False
    primes_set = set()
    phi = p - 1
    for i in range(1, p):
        if pow(g, i, p) in primes_set:
            return False
        primes_set.add(pow(g, i, p))
    return len(primes_set) == phi

# Function to generate the public key
def generate_public_key(g, p, private_key):
    return (g ** private_key) % p

# Function to generate the shared key
def generate_shared_key(public_key, private_key, p):
    return (public_key ** private_key) % p

# Function to encrypt a message
def encrypt_message(message, key):
    encrypted_message = ""
    for char in message:
        encrypted_message += chr(ord(char) + key)
    return encrypted_message

# Function to decrypt a message
def decrypt_message(encrypted_message, key):
    decrypted_message = ""
    for char in encrypted_message:
        decrypted_message += chr(ord(char) - key)
    return decrypted_message

# Main function
def main():
    # Step 1: Ask the user to enter a prime number
    while True:
        try:
            p = int(input("Enter a prime number: "))
            if not is_prime(p):
                raise ValueError("The entered number is not a prime number.")
            break
        except ValueError as e:
            print(e)


    # Step 2: Ask the user to enter a generator
    while True:
        try:
            g = int(input("Enter a generator (a number less than {}): ".format(p)))
            if g >= p or not is_primitive_root(g, p):
                raise ValueError("The entered number is not a primitive root of {}.".format(p))
            break
        except ValueError as e:
            print(e)

    # Step 3: Ask the user to enter their private key
    while True:
        try:
            private_key = int(input("Enter your private key: "))
            break
        except ValueError:
            print("Invalid input. Please enter an integer.")

    # Step 4: Generate public key from user input
    public_key = generate_public_key(g, p, private_key)

    print("Public key generated:", public_key)

    # Step 5: Receive the other party's public key
    while True:
        try:
            other_public_key = int(input("Enter the received public key: "))
            break
        except ValueError:
            print("Invalid input. Please enter an integer.")

    # Step 6: Generate shared key
    shared_key = generate_shared_key(other_public_key, private_key, p)

    # Step 7: Enter message
    message_to_encrypt = input("Enter your message: ")

    # Step 8: Convert message to ciphertext
    ciphertext = encrypt_message(message_to_encrypt, shared_key)
    print("Ciphertext:", ciphertext)

    # Step 9: Receive the encrypted message and decrypt
    received_encrypted_message = input("Enter the received ciphertext message: ")
    decrypted_message = decrypt_message(received_encrypted_message, shared_key)
    print("Decrypted message:", decrypted_message)

if __name__ == "__main__":
    main()
