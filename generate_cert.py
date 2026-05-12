#!/usr/bin/env python3
"""
Generate self-signed SSL certificate for HTTPS development.
Creates certs/server.crt and certs/server.key
"""

import os
from pathlib import Path
from datetime import datetime, timedelta
from cryptography import x509
from cryptography.x509.oid import NameOID
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives.asymmetric import rsa
from cryptography.hazmat.primitives import serialization


def generate_self_signed_cert():
    """Generate a self-signed certificate for localhost."""
    
    certs_dir = Path("certs")
    certs_dir.mkdir(exist_ok=True)
    
    cert_file = certs_dir / "server.crt"
    key_file = certs_dir / "server.key"
    
    # Check if certificate already exists
    if cert_file.exists() and key_file.exists():
        print(f"✓ Certificates already exist at {cert_file} and {key_file}")
        return
    
    print("Generating self-signed certificate for localhost...")
    
    # Generate private key
    private_key = rsa.generate_private_key(
        public_exponent=65537,
        key_size=2048,
        backend=default_backend(),
    )
    
    # Build certificate subject and issuer
    subject = issuer = x509.Name([
        x509.NameAttribute(NameOID.COUNTRY_NAME, "US"),
        x509.NameAttribute(NameOID.STATE_OR_PROVINCE_NAME, "State"),
        x509.NameAttribute(NameOID.LOCALITY_NAME, "City"),
        x509.NameAttribute(NameOID.ORGANIZATION_NAME, "Smart Attendance"),
        x509.NameAttribute(NameOID.COMMON_NAME, "localhost"),
    ])
    
    # Create certificate
    cert = x509.CertificateBuilder().subject_name(
        subject
    ).issuer_name(
        issuer
    ).public_key(
        private_key.public_key()
    ).serial_number(
        x509.random_serial_number()
    ).not_valid_before(
        datetime.utcnow()
    ).not_valid_after(
        datetime.utcnow() + timedelta(days=365)
    ).add_extension(
        x509.SubjectAlternativeName([
            x509.DNSName("localhost"),
            x509.DNSName("127.0.0.1"),
            x509.DNSName("*.localhost"),
        ]),
        critical=False,
    ).sign(private_key, hashes.SHA256(), default_backend())
    
    # Write certificate to file
    with open(cert_file, "wb") as f:
        f.write(cert.public_bytes(serialization.Encoding.PEM))
    
    # Write private key to file
    with open(key_file, "wb") as f:
        f.write(private_key.private_bytes(
            encoding=serialization.Encoding.PEM,
            format=serialization.PrivateFormat.TraditionalOpenSSL,
            encryption_algorithm=serialization.NoEncryption(),
        ))
    
    print(f"✓ Generated certificate: {cert_file}")
    print(f"✓ Generated private key: {key_file}")
    print("\n⚠️  Note: This is a self-signed certificate for development only.")
    print("   Browsers will show a security warning when first accessing https://localhost")
    print("   Accept the exception in your browser to proceed.\n")


if __name__ == "__main__":
    generate_self_signed_cert()
