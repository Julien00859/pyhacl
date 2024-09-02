import unittest
from pyhacl.key_exchange import curve25519_51, curve25519_64

class TestKeyExchange(unittest.TestCase):
    def test_ed25519(self):
        alice_sk = b'a' * 32
        alice_pk = curve25519_51.secret_to_public(alice_sk)

        bob_sk = b'b' * 32
        bob_pk = curve25519_64.secret_to_public(bob_sk)

        shared1 = curve25519_51.ecdh(alice_sk, bob_pk)
        shared2 = curve25519_64.ecdh(bob_sk, alice_pk)

        self.assertEqual(shared1, shared2)
