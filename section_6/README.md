# Bitcoin and Blockchain 
Bitcoin, a digital currency originating in 2008, has experienced a remarkable surge in value over the past decade, skyrocketing from mere cents to nearly 20 thousand dollars per bitcoin. This exponential growth underscores Bitcoin's widespread adoption globally, finding acceptance in various countries, stores, and financial institutions. However, beyond its financial implications, the true innovation lies in the groundbreaking technology underpinning Bitcoin – the blockchain.

## Cryptography Foundation and Bitcoin Address

Bitcoin, as a cryptocurrency, relies on a cryptographic foundation, utilizing one-way hash functions and public-key cryptography. This section explores the manual generation of a Bitcoin address, a crucial element in its decentralized system, where no central authority or account creation is necessary.

*Generating Private and Public Keys*

Bitcoin employs Elliptic Curve Cryptography (ECC), specifically the secp256k1 curve, known for its efficiency and security advantages. ECC, based on elliptic curves over finite fields, offers shorter keys and signatures compared to non-EC cryptography like RSA.

**Algorithm:**
- The curve equation for secp256k1: \(y^2 = x^3 + 7\).
- Public keys are coordinates (x, y) on this curve, derived from the private key, a 32-byte random number.

**Generating Private and Public Keys:**
- OpenSSL command: `openssl ecparam -name secp256k1 -genkey -out privkey.pem`.
- The output file, privkey.pem, includes curve details, the private key, and the public key in Base64 encoding.

Understanding these cryptographic underpinnings is essential for comprehending Bitcoin's secure and decentralized nature.

The output file privkey.pem includes the curve name (secp256k1), the private key, and the public key. The file is Base64 encoded, to see its content, we can run the fo llowing command to decode it. 

```bash
openssl ec -in privkey.pem -text -noout 
```

Generates:

```
read EC key
Private-Key: (256 bit)
priv:
    cc:50:a1:68:f8:d3:3f:c7:54:c5:5c:e6:cc:ac:6e:
    0f:ce:0d:5c:57:17:0d:b9:96:08:e8:51:dd:4f:dd:
    9a:60
pub:
    04:42:0b:ac:87:b9:3d:a2:35:fa:01:15:0b:ae:d4:
    86:88:cd:64:11:a4:fc:18:98:04:f5:57:4a:a9:49:
    21:2d:a4:8a:c7:94:bb:44:c6:c1:b7:aa:92:91:e6:
    ec:3b:09:93:d6:e6:8e:08:9b:d1:07:21:9b:21:99:
    db:de:7d:e6:f7
ASN1 OID: secp256k1
```
We can extract the public key component and save it to a different file called pubkey.pem. We can also view the content of the file. 

```bash
openssl ec -in privkey.pem -pubout -out pubkey.pem
openssl ec -in pubkey.pem -pubin -text -noout
```

Generates:

```
ext -noout
read EC key
writing EC key
read EC key
Public-Key: (256 bit)
pub:
    04:42:0b:ac:87:b9:3d:a2:35:fa:01:15:0b:ae:d4:
    86:88:cd:64:11:a4:fc:18:98:04:f5:57:4a:a9:49:
    21:2d:a4:8a:c7:94:bb:44:c6:c1:b7:aa:92:91:e6:
    ec:3b:09:93:d6:e6:8e:08:9b:d1:07:21:9b:21:99:
    db:de:7d:e6:f7
ASN1 OID: secp256k1
```

Bitcoin employs a 65-byte public key, composed of a constant 0x04 prefix, a 32-byte x-coordinate, and a 32-byte y-coordinate. To conserve space, Bitcoin's default format is a compressed public key, omitting the redundant y-value. This compression involves using a prefix byte to denote whether the y-value is positive (0x02) or negative (0x03).

For an uncompressed public key, the prefix is consistently 0x04. In compressed form, the first byte becomes 0x02 for a positive y-value and 0x03 for a negative y-value. The choice is based on the even or odd nature of the y-coordinate, with even indicating positive and odd indicating negative.

This compression simplifies the representation of public keys, optimizing storage and enhancing efficiency in the Bitcoin network.

We can construct the compressed public key very easily using the algorithm described above. We can also use the following command to get the compressed public key.

```bash
openssl ec -in pubkey.pem -pubin -text -noout -conv_form compressed
```

Generates:

```
read EC key
Public-Key: (256 bit)
pub:
    03:42:0b:ac:87:b9:3d:a2:35:fa:01:15:0b:ae:d4:
    86:88:cd:64:11:a4:fc:18:98:04:f5:57:4a:a9:49:
    21:2d:a4
ASN1 OID: secp256k1
```

To facilitate further operations, the compressed public key in colon-separated format needs conversion into a hex string. This conversion involves copying the public key part into a temporary file and eliminating colons and spaces. This can be done manually or by using the `tr` command, which efficiently removes all characters except letters and digits. This preparatory step ensures a clean and usable hex string representation for subsequent cryptographic operations.

```bash
tr -dc '[:alnum:]' < temp
# %
```

Generate Public-key hash. The Bitcoin network uses the hash value of public keys in transactions, instead of directly using public keys. To generate a hash from a public key, we need to apply two hash algorithms on the public key: SHA256 and RIPEMDl 60. The result is a 160-bit hash value (20 bytes). This number can be used in Bitcoin transactions. The following command can generate the hash value

```bash
$ echo 6e3c5c2c10d5d53c4e52d00aef53e73e158977eba3fd9e51b36437564c88c8d0 | xxd -r -p | openssl dgst -sha256 -binary | openssl dgst -ripemd160

# (stdin) = 6e3c5c2c10d5d53c4e52d00aef53e73e158977eba3fd9e51b36437564c88c8d0

```

Bitcoin Address and Encoding

To receive payment in Bitcoin, the payee provides a Bitcoin address to the payer. The address, often a 20-byte hash value, can be derived from the hash of the payee's public key. Another payment type, Pay-to-ScriptHash (P2SH), uses the hash value of a script as the address.
Sending a 20-byte hash value poses challenges, especially in practical situations where errors can occur. The hexadecimal or decimal forms may not be the most user-friendly representations. Bitcoin addresses need to be conveyed accurately, as mistakes in transactions can lead to irreversible losses.
Bitcoin employs Base58 as its encoding scheme for addresses. Unlike Base64, Base58 omits certain characters to avoid confusion, such as 0 (zero), O (capital o), I (capital i), l (lower case L), + (plus), and / (slash). This encoding ensures a more user-friendly representation.
Detecting mistyped addresses is crucial in Bitcoin transactions. Base58Check, the modified version of Base58, adds a checksum to the binary data before encoding. A version number is also appended to the public key hash, with O indicating Pay-to-pubkey-hash type, and 05 indicating Pay-to-script-hash type. The checksum enables the immediate identification of errors in an address, preventing invalid transactions and irreversible losses.

## Transactions

*Safe Analogy*
In Bitcoin transactions, the movement of money is likened to transferring funds from one safe (input) to another safe (output). Each safe is locked, and unlocking requires the correct "key," often in the form of a signature and public key. The analogy helps understand that bitcoins don't move between accounts but rather change ownership from one "safe" to another.

*Locking Mechanisms*
Bitcoin utilizes various locking mechanisms, with a primary one being the public key hash. A safe locked by a public key hash requires the correct public key and a corresponding signature to be unlocked. Another interesting mechanism allows a safe to be locked by multiple keys, requiring a subset of them to be unlocked to access the funds.

Compared to traditional banking, Bitcoin's use of safes offers several advantages:
- **Decentralization:** Anyone can create a safe without needing central authority, enabling easy and direct transactions.
- **Transparency:** The contents of a safe are visible to everyone, enhancing transparency.
- **Anonymity:** Bitcoin safes provide a level of anonymity, making it challenging to trace transactions back to individuals.
A Bitcoin transaction consists of two parts: input and output.
- **Output:** Specifies where the funds go. It can include multiple outputs, each acting like a new safe. Any leftover funds can be sent to the user's own safe as "change."

*Transaction*
Using an example where Alice pays Bob and Charlie, the inputs reference past transactions, specifying the source of funds. The outputs allocate funds to recipients (Bob and Charlie) and include a "change" output for Alice. This change, intentionally less than the leftover amount, serves as a transaction fee for miners who validate and include the transaction in a block.

*Transaction Fee*
The unclaimed portion of the leftover amount in the "change" output acts as a transaction fee. Miners collect these fees, providing an incentive to include transactions in blocks. Without transaction fees, miners might not prioritize certain transactions, leading to delays in recognition and fund transfer.

## Unlocking the Output of a Transaction

**Unlocking the Output of a Transaction:**
   - Outputs of transactions act like locked safes.
   - Bitcoin uses programmable locks (Script) allowing users to create their own locks and keys.
   - Locking scripts are called PubKey Scripts; unlocking scripts are called scriptSig.
   - The combination of locking and unlocking scripts determines the validity of a transaction.

**Script in Bitcoin:**
   - Script is a basic programming language in Bitcoin.
   - It consists of data (public keys, signatures) and opcodes.
   - Stack-based execution from left to right.
   - Script is intentionally not Turing-complete to avoid infinite loops.

**Some Fun but Non-standard Locks:**
   - Examples of non-standard script types: Anyone-Can-Spend, No-One-Can-Spend (Bitcoin Burning), Math Puzzle, Transaction Puzzle.
   - These demonstrate various ways to lock and unlock transactions.

**Pay-to-Pubkey-Hash Type (P2PH):**
   - Common form of Bitcoin transactions.
   - Involves a payment to the hash of the recipient's public key.
   - Requires providing the public key and a signature for spending.

**Pay-to-Multisig (P2MS):**
   - Payment to a group, requiring approval from a subset of members.
   - Example: 2 out of 3 people must sign to spend the funds.

**Pay-to-ScriptHash (P2SH):**
   - Introduction of a new way to build safes, shifting responsibility to payees.
   - Instead of providing the entire script, payees provide the hash.
   - Reduced transaction size and increased security.

**P2SH Example: Multi-Signature:**
   - Demonstrates using P2SH to implement a multi-signature transaction.
   - Simplifies the process for the payee and reduces transaction size.

**Case Study: A Real Transaction:**
   - Analysis of a real Bitcoin transaction, including inputs, outputs, scriptPubKey, and scriptSig.
   - Decoded information from a sample transaction.

**Propagation of Transactions:**
   - Transactions need to be broadcast to the entire Bitcoin network for validation and inclusion in blocks.
   - The peer-to-peer network ensures the spread of transactions to all nodes.

## Blockchain and Mining
**Introduction to Blockchain and Mining:**
   - Overview of traditional banking systems and private ledger databases.
   - Introduction to Bitcoin's distributed ledger database (Blockchain).
   - Challenges of achieving consensus and preventing unauthorized modifications.

**Generating Blocks:**
   - Explanation of how transactions are added to the Bitcoin blockchain.
   - Role of miners in creating blocks and the proof-of-work (POW) system.
   - Difficulty in creating valid blocks and the time it takes to create a new block.

**Blockchain Properties:**
   - Blockchain as an append-only distributed database.
   - Use cases beyond cryptocurrencies, such as storing voting or healthcare data.

**Rewarding Mechanism:**
   - Incentives for miners in the form of block rewards.
   - Description of Coinbase transactions and the process of mining.

**Transaction and Merkle Tree:**
   - Merkle tree construction for transaction verification.
   - Efficiency of Merkle trees in verification compared to hashing all transactions.

**Branching and Reaching Consensus:**
   - Challenges of achieving consensus in a distributed blockchain network.
   - Description of branching and how the longest chain is accepted as the correct one.

**Confirmation and Double Spending:**
   - Introduction to confirmation numbers and their significance.
   - Addressing the double-spending problem and factors affecting its probability.
   - Importance of waiting for an adequate number of confirmations for secure transactions.

**Majority of Hash Power:**
   - Impact of miner's hash power on the probability of successful double spending.
   - Analysis of success rates based on hash power and confirmation numbers.
