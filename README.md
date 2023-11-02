# Python-Secure-File-Transfer-with-RSA-Encryption
This Python script provides a secure and encrypted method for transferring files using RSA encryption and SSH. It allows you to generate RSA key pairs, encrypt files, and send them to a remote server while maintaining data confidentiality.
## Prerequisites

Before using this script, make sure you have the following prerequisites installed:

1. **Python**: Ensure that Python is installed on your system. You can download it from [python.org](https://www.python.org/downloads/).

2. **Paramiko**: Install the Paramiko library using pip:

   ```bash
   pip install paramiko
   ```
3. **RSA Library**: Install the RSA library using pip
   ```bash
   pip install rsa
   ```
## Usage

  ### Generating RSA Keys

  Run the script to generate RSA key pairs – a public key and a private key. These keys will be saved as "pubkey.pem" and "privkey.pem" in the script's directory.

  ```bash
  python RSAscript.py
  ```
  You only need to generate keys once. These keys are used for encryption and decryption.

  ### Sending an Encrypted File

  Choose option 1 from the menu to send an encrypted file to a remote server. Provide the path of the file to be encrypted and the recipient's name (e.g., "kali"). The script will encrypt the file and securely send it to the specified remote server.

  ### Decrypting a File

  Choose option 2 from the menu to decrypt a specific file. Provide the path of the encrypted file you wish to decrypt. If the file was encrypted with the correct recipient name, the script will decrypt it using the private key and display the plaintext content.

  #### Note: If the recipient name is incorrect or the file was not encrypted with the correct recipient's public key, decryption will fail.

  ### Configuration

  Ensure that the SSH service (including SFTP) is running on the remote server where you want to send files. Verify the SSH server's status and confirm that the recipient's hostname, username, and password are correctly provided in the script.

  Make sure the "Kali_pubkey.pem" file exists and contains the recipient's public key. Adjust the recipient's hostname, username, and password in the SSH connection settings within the script.
  #### Note: Replace RSAscript.py with the actual name of your Python script
  # Disclaimer
  This script is intended for educational and demonstration purposes. Always use it in compliance with ethical guidelines and obtain necessary permissions for any remote server access.
  

  
