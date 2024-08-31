import sys

from .hashlib import sha256

def main():
    if len(sys.argv) != 2:
        return f"usage: {__package__} <data>"

    sha = sha256(sys.argv[1].encode())
    sha2 = sha.copy()
    print(sha.digest().hex())
    print(sha2.digest().hex())
    sha2.update(b'hello')
    print(sha.digest().hex())
    print(sha2.digest().hex())
    print(1)
    del sha
    print(2)
    del sha2
    print(3)

sys.exit(main())
