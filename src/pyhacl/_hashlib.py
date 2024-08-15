import cython
from cython.cimports.libc.stdint import uint8_t
from cython.cimports.pyhacl.include.hacl_hash_sha2 import Hacl_Hash_SHA2_hash_256

def sha256(data: bytes) -> bytes:
    output: cython.char[33]
    output[32] = 0
    Hacl_Hash_SHA2_hash_256(
        cython.cast(cython.pointer(uint8_t), output),
        cython.cast(cython.pointer(uint8_t), data),
        len(data)
    )
    return output
