import os
import sys

from .key_exchange import curve25519_51, curve25519_64

def main():
    if len(sys.argv) != 2:
        return f"usage: {__package__} <data>"

    alice_sk = os.urandom(32)
    alice_pk = curve25519_51.secret_to_public(alice_sk)

    bob_sk = os.urandom(32)
    bob_pk = curve25519_64.secret_to_public(bob_sk)

    shared1 = curve25519_51.ecdh(alice_sk, bob_pk)
    shared2 = curve25519_64.ecdh(bob_sk, alice_pk)

    print(shared1)
    print(shared2)


sys.exit(main())
