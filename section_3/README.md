# Public Key Cryptography

## Diffie-Hellman Key Exchange
The Diffie-Hellman key exchange enables secure key generation over an insecure channel for parties with no prior knowledge of each other. This section explores the workings of this protocol, emphasizing its foundational role in public-key cryptography. It also outlines a slight modification that transforms it into a public-key encryption scheme, paving the way for various encryption algorithms.

The Diffie-Hellman (DH) key exchange protocol involves three steps:

1. Selecting Parameters: Alice and Bob agree on a finite cyclic group (p) and a generating element (g). These parameters are non-secret and can be standardized.
2. Exchanging Key Materials: Alice and Bob generate random numbers (x and y) and exchange values (A and B) using modular exponentiation.
3. Computing the Shared Secret: Both parties use received values to compute the shared secret (K), allowing secure communication without transmitting the key.

The DH key exchange protocol can be modified to serve as a public-key encryption scheme:

*Key Generation and Encryption Steps*:
* Alice independently selects parameters, generates a public/private key pair (x, gx mod p), and publishes her public key. Bob, to send a message (m) to Alice, generates a random number (y), computes gY mod p, and uses Alice's public key for encryption.

*Decryption Step*:
* Alice decrypts the received ciphertext using her private key (x) to recover the shared secret (K), enabling secure communication between Alice and Bob.
This modification serves as the basis for public-key encryption algorithms like Elgamal and Integrated Encryption Scheme (IES), contributing to the broader field of public-key cryptography.

## The RSA Algorithm

After the conceptualization of an asymmetric public-private key cryptosystem by Whitfield Diffie and Martin Hellman in 1976, Ron Rivest, Adi Shamir, and Leonard Adleman developed the RSA algorithm in 1978. Named after the inventors' initials, the RSA algorithm relies on the mathematical complexity of factoring large prime numbers for security. In this section, we delve into the details of RSA, covering key generation, encryption, and decryption.

Key Generation:

* Choose two large prime numbers (p and q).
* Compute n = pq and Euler's totient function (φ(n)).
* Select a public exponent (e) coprime to φ(n).
* Calculate the private exponent (d) as the modular inverse of e modulo φ(n).
* Public key: (e, n), Private key: (d, n).

Encryption:

* Convert plaintext message (M) to an integer.
* Encrypt M using the public key (e, n) with the formula C ≡ M^e (mod n).
* Transmit the ciphertext (C).

Decryption:

* Use the private key (d, n) to decrypt the ciphertext (C).
* Recover the original message M with the formula M ≡ C^d (mod n).

Security relies on the difficulty of factoring large numbers. The RSA algorithm involves modulo operations, Euler's theorem, and the extended Euclidean algorithm.

## Paddings for RSA

In practical applications, a hybrid approach is employed, involving a content key encrypted with a secret-key algorithm and then using RSA to encrypt the content key. Plain RSA, where plaintext is treated as a number and directly encrypted, faces vulnerabilities.

*Hybrid Approach*: Combines content key and secret-key encryption with RSA for practical implementation.
Plain RSA Vulnerabilities:
* Deterministic encryption.
* Weaknesses when e is small.
* Vulnerability to certain attacks.

## Digital Signature
Using a private key to generate a signature and public key to verify.

Digital Signature using RSA

RSA algorithm property: Applying public-key then private-key operation retrieves the original message.
Usefulness for encryption and signature generation.
Signature generation process: 
s = m^d mod n where m is the message.

## Applications
*Authentication*:

Public keys play a crucial role in authentication. Common method: Password authentication, involving the exchange of secrets between parties A and B. Despite widespread use, password authentication has drawbacks.

Disadvantages of Password Authentication:

* Vulnerability when using the same password across multiple accounts.
* Inability to authenticate a single party by many parties.
* Servers can authenticate clients, but clients cannot authenticate servers due to the shared secret issue.

Shared Secret Dependency

Password authentication relies on a shared secret, akin to the vulnerability in secret-key encryption.
Public key cryptography addresses this issue by using different keys for encryption and decryption.

Public-Key Based Authentication

A (being authenticated) receives a challenge from B, signs it using A's private key, and sends the signature back to B.
B verifies the signature using A's public key; successful verification authenticates A.