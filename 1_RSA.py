# RSA Algorithm in cryptography

def gcd(a, b):
    gcd_val = 0
    for i in range(1, min(a, b) + 1):
        if (a % i == 0) and (b % i == 0):
            gcd_val = i
    return gcd_val

# Encryption Exponent 
def e_value(fin):
    e_val = 0 
    # 1 < e < ϕ(n) (fin)
    for i in range(2, fin):
        if gcd(i, fin) == 1:
            e_val = i
            break
    return e_val


# Decryption Exponent
def d_value(phi_n_val, e_val):
    d_val = 0
    for i in range(1, 10000):
        d_val = int((1 + i * phi_n_val) / e_val)
        # d = e^-1 mod ϕ(n) or we can define it as ed = 1 mod ϕ(n)
        if 1 < d_val < phi_n_val and (e_val * d_val) % phi_n_val == 1:
            break
        else:
            pass
    return d_val

def encrypt_message(message, e, n):
    # Convert each character to its ASCII value and encrypt
    encrypted_chars = [(ord(char) ** e) % n for char in message]
    return encrypted_chars

def decrypt_message(encrypted_message, d, n):
    # Decrypt each character and convert back to ASCII value
    decrypted_chars = [chr((char ** d) % n) for char in encrypted_message]
    return ''.join(decrypted_chars)


p = int(input("Enter Value of p (Large Prime Number):  "))
q = int(input("Enter Value of q (Large Prime Number):  "))
message = input("Enter Message:  ")

n = p * q
phi_n = (p - 1) * (q - 1)

e = e_value(phi_n)
d = d_value(phi_n, e)

print("Public Key: (", e, ",", n, ")")
print("Private Key: (", d, ",", n, ")")

print("----------------------------------------------")
encrypted_message = encrypt_message(message, e, n)
print("Encrypted Text:", encrypted_message)

private_key_input = input("Enter the private key to decrypt the message (format: #,#): ")
private_key_parts = private_key_input.split(",")
if len(private_key_parts) == 2:
    private_key_d = int(private_key_parts[0])
    private_key_n = int(private_key_parts[1])
    
    if private_key_d == d and private_key_n == n:
        decrypted_message = decrypt_message(encrypted_message, d, n)
        print("Decrypted Message:", decrypted_message)
    else:
        print("Invalid private key!")
else:
    print("Invalid private key format!")
