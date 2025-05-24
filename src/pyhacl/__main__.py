import os
import sys

from .aead import chacha_poly1305
from .hashlib import sha256
from .key_exchange import curve25519_64
from .signature import p256

def main():
    if len(sys.argv) != 2:
        return f"usage: {__package__} <data>"
    data = sys.argv[1].encode()

    print("pyhacl demo")

    # Hashlib
    sha = sha256.oneshot(data)
    print(
        "\nHashlib"
        "\nsha256", sha
    )

    # AEAD
    key = os.urandom(32)
    nonce = (0).to_bytes(12, 'big')
    cipher, tag = chacha_poly1305.encrypt(
        data, sha, key, nonce
    )
    text = chacha_poly1305.decrypt(
        cipher, sha, key, nonce, tag
    )
    print(
      "\nAEAD"
      "\nrandom key", key,
      "\nnonce", nonce,
      "\nchapoly cipher", cipher,
      "\nchapoly tag", tag,
      "\ndecrypted back", text,
    )

    # Signature
    p256_priv = bytes.fromhex(
        '3813E9CC1168AED230DCA65AF0F0BF3EAF2D48A3495777A0D865D4CE1E0094E0')
    assert p256.validate_private_key(p256_priv)
    p256_pub = p256.uncompressed_to_raw(bytes.fromhex(
        '047BD9F4AA8801613D81C73B9480347D0A6AB4AF7EB1B04EB634151477EB651E'
        'D6CBBC6251D01C0CD52E5FDC1B44C9AC544059FAC6398EE1DA4F4382E356A4D9'
        'C9'))
    assert p256.validate_public_key(p256_pub)

    signature = p256.sign_sha2(cipher, p256_priv, b'a' * 32)
    print(
        "\nSignature"
        "\np256", len(signature), signature
    )
    assert p256.verif_sha2(cipher, p256_pub, signature)

    # Key exchange
    alice_priv = os.urandom(32)
    alice_pub = curve25519_64.secret_to_public(alice_priv)
    bob_priv = os.urandom(32)
    bob_pub = curve25519_64.secret_to_public(bob_priv)
    alice_shared = curve25519_64.ecdh(alice_priv, bob_pub)
    bob_shared = curve25519_64.ecdh(bob_priv, alice_pub)
    print(
        "\nKey Exchange",
        "\nalice",
        "\n\tpriv", alice_priv,
        "\n\tpub", alice_pub,
        "\nbob"
        "\n\tpriv", bob_priv,
        "\n\tpub", bob_pub,
        "\nshared secret",
        "\n\talice", alice_shared,
        "\n\tbob", bob_shared,
    )


sys.exit(main())
