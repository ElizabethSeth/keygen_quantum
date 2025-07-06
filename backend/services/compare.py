from Crypto.Random import get_random_bytes
from backend.services.entropy import analyze_key

def generate_random_key(length_bits: int = 256) -> str:
    byte_len = length_bits // 8
    key_bytes = get_random_bytes(byte_len)
    return ''.join(f'{byte:08b}' for byte in key_bytes)


def compare_with_ntru() -> dict:
    # Заглушка: можно заменить на вызов PQClean NTRU
    ml_key_bin = generate_random_key()
    ntru_key_bin = generate_random_key()  # в реальности: ntru_key = PQClean.generate()

    ml_analysis = analyze_key(ml_key_bin)
    ntru_analysis = analyze_key(ntru_key_bin)

    return {
        'ml_key': {
            'key_hex': hex(int(ml_key_bin, 2))[2:],
            **ml_analysis
        },
        'ntru_key': {
            'key_hex': hex(int(ntru_key_bin, 2))[2:],
            **ntru_analysis
        }
    }
