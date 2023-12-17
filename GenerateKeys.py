import secrets

def generate_aes_key(key_length):
    return secrets.token_bytes(key_length)

# Generate AES keys of specified lengths
aes_128_key = generate_aes_key(16)  # 16 bytes for AES-128
aes_192_key = generate_aes_key(24)  # 24 bytes for AES-192
aes_256_key = generate_aes_key(32)  # 32 bytes for AES-256

# Display the generated keys
print("AES-128 Key:", aes_128_key)
print("AES-192 Key:", aes_192_key)
print("AES-256 Key:", aes_256_key)
