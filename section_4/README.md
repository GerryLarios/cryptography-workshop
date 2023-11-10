# Public Key Infrastructure 
Public key cryptography is foundational for secure communication. Vulnerable to man-in-the-middle attacks when one party sends its public key to the other.

The challenge is verifying the ownership of a public key and ensuring it belongs to the claimed owner.
PKI is a practical solution to the ownership verification problem with Certificates, Certificate Authority (CA), and Digital Signature (DS).

## Attack on Public Key Cryptography
*Background on Public Key Cryptography*
Before public key cryptography, encryption relied on secret keys, posing challenges in key exchange.  Public key cryptography resolved this by allowing public sharing of keys. Despite defeating eavesdropping attacks, public key cryptography remains vulnerable to man-in-the-middle (MITM) attacks.

*Man-in-the-Middle (MITM) Attack*

MITM attack occurs when an interceptor manipulates communication between two devices.
Public key exchange susceptible to MITM attacks, compromising security.

MITM attack's fundamental problem: inability to verify if a received public key truly belongs to the claimed owner. The Introduction of digital signatures as a solution, ensuring data integrity and authenticity.

*Public Key Infrastructure (PKI)*

CA's role in verifying user identities and issuing signed digital certificates. Digital Certificates as documents proving ownership of public keys, signed by trusted CAs. The scalability and broader application of PKI in providing a solution beyond local scenarios.

## Public Key Certificates

A public key certificate certifies ownership of a public key, including the owner's identity and a signature from a trusted party. The X.509 standard defines the structure of such certificates. Key components include:

* Issuer: Contains information about the Certificate Authority (CA) issuing the certificate (e.g., Digicert).
* Subject: Holds the owner's information, certifying that the enclosed public key belongs to the specified subject (e.g., Paypal).
* Public Key: Contains the actual public key, such as a 2048-bit RSA key with modulus and exponent.
* Signature: Includes the digital signature of the issuer, using algorithms like Sha256 and RSA.
* Validity: Specifies the certificate's validity period.
* Serial Number: Uniquely identifies each certificate.
* Extensions: Optional fields for additional information.

X.509 certificates often use Base64 encoding for printable characters, typically saved in PEM files. A command-line approach, like the `openssl s_client` command, connects to a server and prints out certificate details

```bash
openssl s_client -showcerts -connect www.paypal.com:443 </dev/null
```

## Certificate Authority (CA)
A Certificate Authority (CA) is a trusted entity that issues signed digital certificates. Verification of the certificate applicant's identity is crucial to the trustworthiness of the Public-Key Infrastructure. The CA performs subject verification, ensuring that the applicant owns or legitimately represents the identity in the subject field of the digital certificate. This may involve domain ownership verification, often achieved through challenges like providing a randomly generated number on a specific web page.

Once the CA verifies the identity information, it signs the certificate, binding the identity to the public key. The signing process involves generating a digital signature for the certificate using the CA's private key. Signatures ensure the certificate's integrity, and anyone with the CA's public key can verify these signatures.

## How PKI Defeats the MITM Attack
The attacker intercepts the TLS handshake between Alice and example.com. The attacker can either forward the authentic certificate from example.com to Alice or create a fake certificate for example.com with the subject field intact but replacing the public key with the attacker's. However, since the attacker lacks the corresponding private key, the TLS session will be established successfully, encrypting a secret that the attacker cannot access. The MITM attack fails.

If the attacker creates a fraudulent certificate for example.com, substituting the public key with their own, the challenge lies in obtaining a valid signature. Trusted certificate authorities won't sign the attacker's request without legitimate ownership of the example.com domain. Compromising a certificate authority is a challenging task. The attacker might resort to a self-signed certificate, but Alice's browser, unable to find a trusted certificate for verification, issues a warning. The user can then decide whether to terminate the connection (thwarting the MITM attack) or proceed at their own risk, potentially falling victim to the attack if they choose to continue.
## Types of Digital Certificates
The role of a Certificate Authority (CA) is crucial in verifying information in the subject field and certifying the ownership of the public key. This involves identity verification and validation, with different levels of effort and cost. There are three main types of certificates:

*Domain Validated Certificate (DV)*:
* Verification Method: Domain Control Validation (DCV)
* Verification Process:
    * Emails: CA sends an email to the administrator email fetched from WHOIS, containing a verification link.
    * HTTP: Hash value of the certificate request is placed in a file on a web server inside the requested domain.
    * DNS: Hash value is entered as a DNS CNAME record for the domain.

*Organizational Validated Certificate (OV)*
* Additional Verification: In addition to domain verification, CAs validate the organization and identity information of the applicant.
* Verification Criteria:
    * Domain control validation.
    * Applicant's identity, address, and link to the organization.
    * Organization's address and WHOIS record.
    * Callback on the organization's verified telephone number.

*Extended Validated Certificate (EV)*
* Enhanced Validation: Requires more extensive validation compared to DV and OV certificates.
* Document Requirement: CAs issuing EV certificates demand legally signed documents from registration authorities, cross-checked by the CA.
Validation Criteria:
    * Domain control validation.
    * Verify the identity, authority, signature, and link of the individual involved.
    * Verify the organization's physical address, telephone number, operational existence, and legal standing.
