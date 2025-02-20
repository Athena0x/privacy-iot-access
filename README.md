
# Privacy-Preserving Access Management System for IoT Devices

This project implements a privacy-preserving single-sign-on (ASSO) system for IoT devices in a sharing economy.
The system uses blind signatures for anonymous authentication and attribute-based fine-grained access control.

## Features
- **Blind Signatures:** Enables anonymous token issuance
- **Attribute-Based Access Control:** Fine-grained permission system
- **Optimized for IoT:** Uses lightweight cryptographic operations
- **Performance Evaluation:** Measures communication and computation efficiency

## Installation
```
pip install -r requirements.txt
python src/server.py
python src/iot_client.py
```

## Usage
1. Start the authentication server.
2. IoT devices request access based on their attributes.
3. The server grants or denies access.


