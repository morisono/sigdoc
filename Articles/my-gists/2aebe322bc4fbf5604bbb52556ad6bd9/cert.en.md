x.509:
X.509 is an international standard that defines the format for public key certificates. Certificates used in SSL/TLS communications, among other things, adhere to the X.509 format. X.509 certificates contain a public key, signature, and information about the certificate owner.

PKCS1 ~ PKCS12:
PKCS (Public-Key Cryptography Standards) is a series of standards that define specifications related to public key cryptography. PKCS was developed by RSA Laboratories. PKCS1 defines methods for RSA key pair generation, encryption/decryption, and more. PKCS12 is a file format used to store keys and certificates, typically protected with a password.

.crt:
.crt is the extension for certificate files. SSL/TLS certificates are usually encoded in PEM format and have the .crt extension. Certificate files (.crt) contain a public key and related information, and they are used in web servers, application servers, and more.

CSR (Certificate Signing Request):
CSR is also known as a Certificate Signing Request. It's a file submitted to a Certificate Authority (CA) to issue an SSL/TLS certificate. CSR includes a public key and organizational information, and the CA uses it to sign the certificate. A CSR typically contains details about the domain and organization.

PEM (Privacy Enhanced Mail):
PEM format is used to represent data in BASE64-encoded text. PEM format is widely used for certificate and private key files. SSL certificates and private keys are often stored in PEM format and commonly have the .pem extension.

DER (Distinguished Encoding Rules):
DER format is a binary encoding format that represents certificates and private keys as byte sequences. DER format is more compact than PEM format and is mainly used as a binary container format.

CER (Certificate):
CER is the extension for certificate files. Certificates are digital documents containing a public key and related information. They are used for authentication and data encryption for specific domains or organizations.
