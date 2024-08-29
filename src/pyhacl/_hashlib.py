# distutils: sources = hacl-packages/src/Hacl_Hash_SHA2.c

import cython
from cython.cimports.libc.stdint import uint8_t
from cython.cimports.libc.string import memcpy

import cython.cimports.pyhacl.include.hacl_hash_sha2 as sha2

def sha256(data: bytes) -> bytes:
    output: cython.char[33]
    output[32] = 0
    sha2.Hacl_Hash_SHA2_hash_256(
        cython.cast(cython.pointer(uint8_t), output),
        cython.cast(cython.pointer(uint8_t), data),
        len(data)
    )
    return output


@cython.cclass
class SHA256:
    _state: cython.pointer(sha2.Hacl_Hash_SHA2_state_t_256)

    def __cinit__(self):
        self._state = sha2.Hacl_Hash_SHA2_malloc_256()
        if not self._state:
            raise MemoryError()

    def __dealloc__(self):
        sha2.Hacl_Hash_SHA2_free_256(self._state)
        self._state = cython.NULL

    def __init__(self, data=b''):
        if data:
            self.update(data)

    def update(self, data: bytes) -> None:
        sha2.Hacl_Hash_SHA2_update_256(
            self._state,
            cython.cast(cython.pointer(uint8_t), data),
            len(data),
        )

    def digest(self) -> bytes:
        output: uint8_t[32]
        sha2.Hacl_Hash_SHA2_digest_256(self._state, output)
        return output[:32]

    def hexdigest(self) -> str:
        return self.digest().hex()

    def copy(self):
        copy: SHA256 = type(self)()
        copy._state[0].block_state[0] = self._state[0].block_state[0]
        memcpy(
            cython.cast(cython.p_void, copy._state[0].buf),
            cython.cast(cython.p_void, self._state[0].buf),
            64,
        )
        copy._state[0].total_len = self._state[0].total_len
        return copy
