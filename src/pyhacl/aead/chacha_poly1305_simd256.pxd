from libc.stdint cimport uint8_t, uint32_t

cdef extern from "Hacl_AEAD_Chacha20Poly1305_Simd256.h":
    void Hacl_AEAD_Chacha20Poly1305_Simd256_encrypt(
        uint8_t *output,
        uint8_t *tag,
        uint8_t *input,
        uint32_t input_len,
        uint8_t *data,
        uint32_t data_len,
        uint8_t *key,
        uint8_t *nonce
    )

    uint32_t Hacl_AEAD_Chacha20Poly1305_Simd256_decrypt(
        uint8_t *output,
        uint8_t *input,
        uint32_t input_len,
        uint8_t *data,
        uint32_t data_len,
        uint8_t *key,
        uint8_t *nonce,
        uint8_t *tag
    )
