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
        output: cython.char[33]
        output[32] = 0
        sha2.Hacl_Hash_SHA2_digest_256(
            self._state,
            cython.cast(cython.pointer(uint8_t), output),
        )
        return output

    def copy(self):
        sha_copy = type(self)()
        memcpy(
            cython.cast(cython.p_void, sha_copy._state),
            cython.cast(cython.p_void, self._state),
            cython.sizeof(sha2.Hacl_Hash_SHA2_state_t_256),
        )
        return sha_copy
