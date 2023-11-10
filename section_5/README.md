# Transport Layer Security
In the current era, a significant volume of data is transmitted via the Internet. However, this poses a risk as data transferred over public networks can be susceptible to unauthorized access or manipulation. To address this concern, applications prioritize securing their communications through encryption and tampering detection. Cryptographic solutions play a crucial role in achieving this security objective, offering various algorithms and parameters. For effective interoperability, applications must adhere to a common standard, and Transport Layer Security (TLS) emerges as such a standard.

1. **Working Mechanism:**
   - TLS serves as a standardized approach for securing data transmissions over the Internet.

2. **Key Focus Areas:**
   - Emphasis on two critical aspects of TLS: handshake and data transmission.

3. **Handshake Process:**
   - Detailed exploration of how two communicating peers establish a secure channel.
   - Highlights cryptographic algorithm selection, certificate verification, and common session key determination.

4. **Data Transmission:**
   - Illustration of data transmission within the established secure channel.
   - Examination of TLS's role in safeguarding data integrity within the secure channel.

5. **Program Development:**
   - Creation of two programs to demonstrate TLS usage.
     - **HTTPS Client:** Fetches web pages from real-world web servers securely.
     - **HTTPS Server:** Provides secure web pages to browsers.

6. **Common Mistakes:**
   - Identification and presentation of common mistakes made by developers when implementing TLS.

## TLS Handshake

Before secure communication between a client and a server can begin, various parameters, such as encryption and key details, must be agreed upon. The TLS Handshake Protocol serves as the primary mechanism for achieving this agreement. This section provides an overview of the protocol, with a focus on certificate verification and key generation.

The TLS Handshake protocol facilitates the agreement between client and server on cryptographic parameters. Key steps include:
- **Client Hello:** Initiates the connection, specifying supported cipher suites and providing a client random string for key generation.
- **Server Hello:** Responds with the chosen cipher suite, server random string, and its public-key certificate.
- **Certificate Exchange:** Server sends its certificate for client verification.
- **Key Exchange:** Client generates a pre-master secret, encrypts it with the server's public key, and sends it to the server.
- **Change Cipher Spec:** Both client and server signal a switch to authenticated and encrypted communication.
- **Finished Messages:** Both parties exchange messages, verifying the success of the handshake.

Certificate verification involves ensuring the validity of the server's certificate. Steps include:
- Checking expiration date and verifying the certificate's signature.
- Client program must have a list of trusted CA certificates.
- Validation failure results in the termination of the TLS connection.

TLS employs public-key cryptography for key exchange, and the process involves three main steps:
1. **Pre-master secret generation:** Client generates a random pre-master secret, encrypted with the server's public key.
2. **Master secret generation:** Using client and server nonces and the pre-master secret, both parties create a master secret.
3. **Session keys generation:** Master secret is utilized to generate bidirectional session keys for encryption and MAC.

TLS allows renegotiation for updating cryptographic parameters. An abbreviated handshake protocol is used for efficiency, involving the generation of new client and server nonces and repeating master secret and session keys generation.

## TLS Data Transmission

After completing the TLS Handshake protocol, client-server pairs can initiate the exchange of application data using the TLS Record protocol. This section delves into the structure of TLS records and the process of sending and receiving data securely.

A TLS record comprises a header and a payload, with the header containing three key fields:
- **Content Type:** Identifies the type of protocol data carried by the record (e.g., Alert, Handshake, Application).
- **Version:** Indicates the major and minor TLS version for the contained message.
- **Length:** Specifies the payload's length, not exceeding 2^14 bytes.

Sending Data with TLS Record Protocol:
1. **Fragment Data:** Break the data into blocks of 214 bytes or less.
2. **Compress Data (Optional):** Compress each block if required.
3. **Add MAC:** Use the MAC key to calculate the MAC of the data, considering the record's sequence number.
4. **Add Padding:** If necessary, add padding to meet block cipher requirements.
5. **Encrypt Data:** Encrypt the data, MAC, and padding using the encryption key, with a random IV at the payload's beginning.
6. **Add TLS Header:** Append the TLS header to the payload.

TLS then writes the constructed record to the TCP stream for transmission.

1. **SSL_read():** Application calls this TLS API to read data from the TLS channel.
2. **Read Records:** SSL_read() invokes the system call read() to read one or multiple records from the TCP stream.
3. **Decrypt and Verify:** Decrypt the records, verify their MAC, and decompress the data if needed.
4. **Buffer Management:** TLS maintains a buffer for handling unused application data.
   - If TLS buffer is empty, retrieve and process one TLS record from the TCP buffer.
   - If more data is required, repeat the process until the request is fulfilled or no more data is available in the TCP buffer.
   - If the TLS buffer is not empty, try to fulfill the request from the buffer; otherwise, return all data in the buffer to the application.
   - Leftover data exceeding the request is stored in the TLS buffer for subsequent read requests.

The TLS Record protocol ensures secure data transmission by structuring records, securing them with encryption and MAC, and managing their reception and processing. Buffering mechanisms enhance efficiency in handling incomplete records and leftover data.
