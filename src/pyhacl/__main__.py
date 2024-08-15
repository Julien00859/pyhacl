import sys

from .hashlib import sha256

def main():
    if len(sys.argv) != 2:
        return f"usage: {__package__} <data>"
    print(sha256(sys.argv[1].encode()).hex())

sys.exit(main())
