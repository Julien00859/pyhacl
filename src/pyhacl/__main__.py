import os
import sys

from .aead import chacha_poly1305
from .hashlib import sha256

def main():
    if len(sys.argv) != 2:
        return f"usage: {__package__} <data>"
    data = sys.argv[1].encode()
    sha = sha256.oneshot(data)

    key = os.urandom(32)
    nonce = (0).to_bytes(12, 'big')

    cipher, tag = chacha_poly1305.encrypt(
        data, sha, key, nonce
    )
    print(len(cipher), cipher)
    print(len(tag), tag)
    text = chacha_poly1305.decrypt(
        cipher, sha, key, nonce, tag
    )
    print(text.decode())


sys.exit(main())
