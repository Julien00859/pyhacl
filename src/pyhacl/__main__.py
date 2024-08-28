import sys

from .hashlib import SHA256

def main():
    if len(sys.argv) != 2:
        return f"usage: {__package__} <data>"

    sha = SHA256(sys.argv[1].encode())
    sha2 = sha.copy()
    sha2.update(b'hello')
    print(sha.digest().hex())
    print(sha2.digest().hex())

sys.exit(main())
