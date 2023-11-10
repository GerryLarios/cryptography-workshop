# Secret-Key Encryption
* Secret-key encryption, also known as symmetric encryption, employs a single key for both the encryption and decryption processes.

* Public-key encryption, or asymmetric encryption, utilizes distinct keys for encryption and decryption operations.

## Substitution Cipher
Classical cryptography involves two main types of ciphers: transposition ciphers and substitution ciphers.

1. Transposition: In transposition ciphers, the arrangement of letters is altered, but the actual identity of the letters remains unchanged.
2. Substitution: Substitution ciphers involve changing the letters themselves, while the positions of the letters remain the same.

There are two main types of substitution ciphers: monoalphabetic and polyalphabetic.

1. Monoalphabetic Cipher: consistent substitution is applied across the entire message.
2. Polyalphabetic Cipher: multiple substitutions at different positions within the message.

Exercise 1.

From the [ciphertext](ciphertext.txt)

```
ytn numrcv cvatmun q lnhn v qnhmnq xb ninayhxcnatvumavi hxyxh ametnh cvatmunq pnfnixenp vup zqnp mu ytn nvhid yx cmpyt anuyzhd yx ehxynay axccnhamvi pmeixcvyma vup cmimyvhd axcczumavymxu numrcv l vq mufnuynp gd ytn rnhcvu nurmunnh vhytzh qatnhgmzq vy ytn nup xb lxhip lvh m nvhid cxpniq lnhn zqnp axccnhamviid bhxc ytn nvhid q vup vpxeynp gd cmimyvhd vup rxfnhucnuy qnhfmanq xb qnfnhvi axzuyhmnq cxqy uxyvgid uvwm rnhcvud gnbxhn vup pzhmur lxhip lvh mm qnfnhvi pmbbnhnuy numrcv cxpniq lnhn ehxpzanp gzy ytn rnhcvu cmimyvhd cxpniq tvfmur v eizrgxvhp lnhn ytn cxqy axceink ovevunqn vup myvimvu cxpniq lnhn viqx mu zqn.
```

Run the following command:

```bash
tr ntyhquvmxbpzfrceiadlkog EHTRSNAIOFDUVGMPLCYWXJB < ciphertext.tx
```

To get the following result:

```
THE ENIGMA MACHINES WERE A SERIES OF ELECTROMECHANICAL ROTOR CIPHER MACHINES DEVELOPED AND USED IN THE EARLY TO MIDTH CENTURY TO PROTECT COMMERCIAL DIPLOMATIC AND MILITARY COMMUNICATION ENIGMA WAS INVENTED BY THE GERMAN ENGINEER ARTHUR SCHERBIUS AT THE END OF WORLD WAR I EARLY MODELS WERE USED COMMERCIALLY FROM THE EARLY S AND ADOPTED BY MILITARY AND GOVERNMENT SERVICES OF SEVERAL COUNTRIES MOST NOTABLY NAwI GERMANY BEFORE AND DURING WORLD WAR II SEVERAL DIFFERENT ENIGMA MODELS WERE PRODUCED BUT THE GERMAN MILITARY MODELS HAVING A PLUGBOARD WERE THE MOST COMPLEX JAPANESE AND ITALIAN MODELS WERE ALSO IN USE.
```

## DES and AES Encryption Algorithm
Concepts of substitution and transposition from classical ciphers are employed in contemporary cryptographic algorithms such as Data Encryption Standard (DES) and (AES) Advanced Encryption Standard.

DES is a block cipher, as opposed to stream cipher that only encrypt a block of data, instead of conducting bit-by-bit encryption conducted by steam ciphers. The size of the block for DES is 64 bits. DES uses 56-bit keys. 

AES was developed because of vulnerabilities revealed in brute force attacks on DES. AES is a block cipher with a 128-bit block size. AES supports key sizes of 128, 192, and 256 bits.

## Encryption Modes

Most encryption algorithms, including DES and AES, operate as block ciphers, encrypting data in fixed-size blocks. DES uses a 64-bit block size, while AES employs a 128-bit block size.

Since plaintexts are typically larger than the block size, a common approach is to divide the plaintext into blocks, encrypt them individually, and then concatenate the results to form the ciphertext.

If two blocks are the same, their encrypted data will also be the same. These identical blocks have helped to preserve the patterns from the original file. One thing that is worth mentioning is that these two pl aintext blocks have to be identical; if they are different in just one bit, from the ciphertext alone, we will not be able to tell how closely related the two plaintext blocks are.

There are many ways to make the inputs di fferent. They are call ed mode of operation or encryption mode. 

*Electronic Codebook (ECB) Mode*: Unsafe method where each block of plaintext is encrypted separately. If two plaintext blocks are identical, their corresponding ciphertext blocks will also be identical.

```bash
openssl enc -aes-128-ecb > -e -in plaintext.txt -out cipher.txt -K 00112233445566778899AABBCCDDEEFF
```

```bash
openssl enc -aes-128-ecb -d -in cipher.txt -out plain2.txt -K 00112233445566778899AABBCCDDEEFF
```

*Cipher Block Chaining (CBC) Mode*: Each block of plantext is XORed with the previous. This way, each ciphertext block depends on all the previous plain text blocks. Therefore, even if two plaintext blocks are the same, the ir previous blocks are never the same. This cipher block uses *Initialization Vector (IV)* to ensure that if two plaintexts are identical, their ciphertexts are still different. By the by, since all the ciphertext blocks are avail able, decryption can be parallelized, we cannot conduct encryption in parallel.

In the following commands, we encrypt the same plaintext using the same key, but with different IVs. From the outcome, we can see that the ciphertexts are very different. If we hadn't known the plaintexts used in the encryption, from the ciphertexts alone, we cannot infer any relationship between the two plaintexts.

Let's see cypher 1:
```bash
openssl enc -aes-128-cbc -e -in plaintext.txt -out cipher1.txt -K 00112233445566778899AABBCCDDEEFF -iv 000102030405060708090a0b0c0d0e0f

xxd -p cipher1.txt
# 1a337fcd56a5299e474dfd4ea4d59b50
```

Let's see cypher 2:
```bash
openssl enc -aes-128-cbc -e -in plaintext.txt -out cipher2.txt -K 00112233445566778899AABBCCDDEEFF -iv 000102030405060708090a0b0c0d0e0e

xxd -p cipher2.txt
# a095a206ba0365e0592673b5ae5c8b5d
```

*Cipher Feedback (CFB) Mode*: The decryption is very similar to encryption: we just "encrypt" the ciphertext from the previous block using the block cipher, and then XOR the outcome with the ciphertext of the current block to generate the plaintext block. A significant property of CFB mode is that it transforms a block cipher into a stream cipher. This allows for the encryption of data bit by bit, eliminating the need to wait for a complete cipher block, making it particularly useful for real-time data and situations with slow data generation.  Due to the bit-wise operation of XOR in CFB mode, padding is not necessary for the last block, simplifying the encryption process. For the same reason as that for the CBC mode, decryption using the CFB mode can be paralleli zed, while encryption can only be conducted sequentially.

```bash
# CBC
openssl enc -aes-128-cbc -e -in plaintext.txt -out cipherl.txt -K 00112233445566778899AABBCCDDEEFF -iv 000102030405060708090a0b0c0d0e0f
# CFB
openssl enc -aes-128-cfb -e -in plaintext.txt -out cipherl.txt -K 00112233445566778899AABBCCDDEEFF -iv 000102030405060708090a0b0c0d0e0f

# Listing files
ls -l plaintext.txt cipher1.txt cipher2.txt

# -rw-r--r-- 1 gerry gerry 32 16 Nov  9 21:20 cipher1.txt
# -rw-r--r-- 1 gerry gerry 21 16 Nov  9 21:24 cipher2.txt
# -rw-r--r-- 1 gerry gerry 21 11 Nov  9 18:09 plaintext.txt
```

*Padding*: Encryption modes require data to be divided into blocks, and the size of each block must align with the cipher's block size. However, there is no guarantee that the last block's size matches the cipher's block size, creating a concern for modes like CBC.
In modes where block sizes must match, such as CBC, padding is needed for the last block. Extra data is added to the last block of the plaintext to ensure its size matches the cipher's block size.

Let us use an experiment to understand how padding works. We will first prepare a file that contains 9 bytes. We encrypt it using the AES algorithm with the CBC mode. The block size of AES is 128 bits (or 16 bytes). 

```bash
# create plain.text
echo -n "123456789" > plain.txt
# encrypt with AES 128 CBC
openssl enc -aes-128-cbc -e -in plain.txt -out cipher.bin -K 00112233445566778899AABBCCDDEEFF -iv 000102030405060708090a0b0c0d0e0e

# Check the size (16)
ls -ld cipher.bin
# -rw-r--r-- 1 gerry gerry 16 Nov  9 21:58 cipher.bin

# decrypt
openssl enc -aes-128-cbc -d -in cipher.bin -out plain2.txt -K 00112233445566778899AABBCCDDEEFF -iv 000102030405060708090a0b0c0d0e0e

# Check the size (9)
ls -ld plain2.txt
# -rw-r--r-- 1 gerry gerry 9 Nov  9 22:04 plain2.txt
```

From the result, we can see that the size of the ciphertext becomes 16 bytes because the padding was added and when we decrypt the ciphertext, the paddings will be removed. How the decryption software know where the padding starts?

```bash
# The enc command has an option called " -nopad", which disables the padding during the decryption
openssl enc -aes-128-cbc -d -in cipher.bin -out plain3.txt -K 00112233445566778899AABBCCDDEEFF -iv 000102030405060708090a0b0c0d0e0e -nopad

# Check the size (9)
ls -ld plain3.txt
# -rw-r--r-- 1 gerry gerry 9 Nov  9 22:04 plain3.txt

# Check the content from the original file
xxd -g 1 plain.txt
# 00000000: 31 32 33 34 35 36 37 38 39                       123456789

# Check the content from the original file
xxd -g 1 plain3.txt
# 00000000: 31 32 33 34 35 36 37 38 39 07 07 07 07 07 07 07  123456789.......
```

From the results above, we can see that 7 bytes of 0x07 are added as the padding data.

## Initialization Vector and Common Mistakes
Many encryption modes necessitate the use of an initialization vector (IV). Unlike encryption keys, IVs are not meant to be secret. This can lead to a misconception that IVs are not as important. Some common mistakes in IV generation include using a fixed value, such as a block of zeros, or employing different values with a predictable pattern. These practices can undermine the security of the encryption process.
An essential requirement for IVs is uniqueness. This implies that no IV should be reused under the same key. Reusing an IV for the same key and plaintext results in identical ciphertexts, and this repetition can lead to unintended disclosure of information.

We use the following experiment to show how to find out P2 using P 1, CI , and C2. The following commands generate these four numbers. It should be noted that the same IV is used when encrypting PI and P2.

```bash
echo -n "This is a known message" > P1
echo -n "Here is a top secret." > P2

openssl enc -aes-128-ofb -e -in P1 -out C1 -K 00112233445566778899AABBCCDDEEFF -iv 00000000000000000000000000000000

openssl enc -aes-128-ofb -e -in P2 -out C2 -K 00112233445566778899AABBCCDDEEFF -iv 0000000000000000000000000000000

# Convert the data to hex strings
xxd -p P1
# 546869732069732061206b6e6f776e206d657373616765
xxd -p C1
# a98c92dd6a6093008ed749f8f0f4ed0b82bdb005acdddd
xxd -p C2
# b58189cb6a6093008ed756f9efa3f04e8caaa602e3

# XOR P1 with C1
python3 xor.py 546869732069732061206b6e6f776e206d657373616765 a98c92dd6a6093008ed749f8f0f4ed0b82bdb005acdddd
# fde4fbae4a09e020eff722969f83832befd8c376cdbab8

# XOR outout with C2
python3 xor.py b58189cb6a6093008ed756f9efa3f04e8caaa602e3 fde4fbae4a09e020eff722969f83832befd8c376cdbab8
# 48657265206973206120746f70207365637265742e

# Convert the hex string to ascii string 
echo -n "48657265206973206120746f70207365637265742e" | xxd -r -p
# Here's a top secret.
```
## Authenticated Encryption and the GCM Mode

To ensure integrity, the sender generates a Message Authentication Code (MAC) from the ciphertext, utilizing a secret shared between the sender and the receiver.

The generated MAC, along with the ciphertext, is transmitted to the receiver. The receiver independently computes its own MAC from the received ciphertext. If the computed MAC matches the received MAC, it indicates that the ciphertext has not been modified.

*Traditional Method using HMAC*: This approach involves using the HMAC algorithm, which is based on one-way hash functions. Traditional Method using HMAC: One drawback of using HMAC is the need for two operations: one for encrypting data and the other for generating the MAC.