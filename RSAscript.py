# Import necessary libraries
import rsa  # Import the RSA encryption library
import paramiko  # Import the Paramiko library for SSH functionality

# Define a function to generate RSA keys
def generate_keys():
    # Method used to generate the private key and public key
    pubKey, privKey = rsa.newkeys(1024)  # Generate new RSA keys with a 1024-bit key length
    
    # Save the public key to a PEM file
    with open('pubkey.pem', 'wb') as f:
        f.write(pubKey.save_pkcs1('PEM'))

    # Save the private key to a PEM file
    with open('privkey.pem', 'wb') as f:
        f.write(privKey.save_pkcs1('PEM'))

# Define a function to load existing RSA keys from PEM files
def load_keys():
    # This method is used to read the public and private keys from the PEM files
    with open('pubkey.pem', 'rb') as f:
        pubKey = rsa.PublicKey.load_pkcs1(f.read())

    with open('privkey.pem', 'rb') as f:
        privKey = rsa.PrivateKey.load_pkcs1(f.read())

    return pubKey, privKey

# Define a function to encrypt a file
def encrypt(file, key):
    msg = open(file, "r").read()  # Read the content of the input file
    
    if key == "kali":
        with open('Kali_pubkey.pem', 'rb') as f:
            pub_Key = rsa.PublicKey.load_pkcs1(f.read())  # Load the recipient's public key
    else:
        print(f"Sorry, We Don't Have The Public key for {key}")
        return

    # Encrypt the message using the recipient's public key
    cText = rsa.encrypt(msg.encode('ascii'), pub_Key)

    f = open("encrypted.txt", "wb")
    f.write(cText)  # Write the encrypted data to a file

    return cText

# Define a function to decrypt a file
def decrypt(file, key):
    ciphertext = open(file, "rb").read()  # Read the content of the encrypted file
    try:
        return rsa.decrypt(ciphertext, key).decode('ascii')  # Decrypt the ciphertext using the private key
    except:
        return False

# Define a function to send a file using SSH
def send_file(file, host):
    ssh = paramiko.SSHClient()  # Create an SSH client
    ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())  # Automatically add the host to known_hosts file
    
    # Establish an SSH connection to the recipient's server
    ssh.connect(hostname="192.168.134.128", username="kali", password="kali")  # Enter the recipient's hostname, username, and password

    ftp = ssh.open_sftp()  # Open an SFTP session for secure file transfer
    
    # Upload the encrypted file to the recipient's server
    ftp.put("encrypted.txt", "/home/kali/project")  # Specify the destination path for the file on the recipient's server
    ftp.close()
    ssh.close()
    print(f"The File {file} Was Uploaded Successfully to {host}")

# Generate RSA keys (call this method the first time you run the program)
generate_keys()

# Load the keys from the files
pubKey, privKey = load_keys()

# Main Menu
print("Please choose an option:")
print("1. Send A File")
print("2. Decrypt A File")
#print("Please enter the name of the file you wish to open, including the file extension. For example, myfile.txt")
choice = input("")

# First Choice Is Send An Encrypted File
if choice == "1":
    # Provide the path of the file to be encrypted
    print("Please enter the name of the file you wish to open, including the file extension. For example, myfile.txt")
    file = input('Enter a File name:')
    recipient = input("Enter the recipient name:")
    ciphertext = encrypt(file, recipient)
    send_file(file, recipient)

# Second choice to decrypt a specific file
if choice == "2":
    # Provide the path of the file to be decrypted
    file = input('Enter a File name:')
    plaintext = decrypt(file, privKey)

    if plaintext:
        print(f'Plain text: {plaintext}')
    if plaintext == False:
        print("The Public Key Used To Encrypt Is Not Yours")
