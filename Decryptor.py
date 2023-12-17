from Crypto.Cipher import AES

# Read the encrypted .dat file as bytes
with open("download-32Bytes.dat", "rb") as f:
    data = f.read()

# The key and IV should be 16 and 16 bytes long respectively
key = b"hjkloahjkiomlehjson5lo0`klsjui3`"
iv = b"0000000000000000"

# The decryption function
def decryptFile(key, iv, encrypted_data):
    # Check if the key and IV meet the required byte length
    if (len(key) == 16 or len(key) == 24 or len(key) == 32) and len(iv) == 16:
        # Create a new AES cipher object in CBC mode
        cipher = AES.new(key, AES.MODE_CBC, iv)

        # Decrypt the data and remove any padding
        decrypted = cipher.decrypt(encrypted_data)
        unpadded = decrypted[:-decrypted[-1]]

        # Check if the unpadded data can be decoded as UTF-8
        try:
            decrypted_text = unpadded.decode('utf-8')
            with open("DecryptedText.txt", "w") as out:
                out.write(decrypted_text)
            # Convert the key into a string and save it into the working_keys
            working_keys = "Key: " + key.decode('utf-8') + "\nIV: " + iv.decode('utf-8')
            with open("WorkingKeys.txt", "w") as out:
                out.write(working_keys)
            print(decrypted_text)
        except UnicodeDecodeError:
            print("Decryption resulted in non-UTF-8 data")
            return
    else:
        print("Key and IV should be 16 bytes long.")
        return  # Exit the function if requirements are not met

decryptFile(key, iv, data)
