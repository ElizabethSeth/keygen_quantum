import math
from collections import Counter


def shannon_entropy(bitstring: str) -> float:
    counts = Counter(bitstring)
    total = len(bitstring)
    entropy = 0.0
    for count in counts.values():
        p_x = count / total
        entropy -= p_x * math.log2(p_x)
    return entropy


def min_entropy(bitstring: str) -> float:
    counts = Counter(bitstring)
    max_p = max(counts.values()) / len(bitstring)
    return -math.log2(max_p)


def bit_ratio(bitstring: str) -> dict:
    total = len(bitstring)
    counts = Counter(bitstring)
    return {
        '0': round(counts.get('0', 0) / total, 3),
        '1': round(counts.get('1', 0) / total, 3)
    }


def analyze_key(bitstring: str) -> dict:
    entropy = shannon_entropy(bitstring)
    minent = min_entropy(bitstring)
    ratio = bit_ratio(bitstring)

    # Простая проверка "прохода" по псевдо-NIST критерию: 
    # энтропия > 7.5 и сбалансированность битов
    nist_passed = entropy > 7.5 and abs(ratio['0'] - ratio['1']) < 0.1

    return {
        'entropy': round(entropy, 4),
        'min_entropy': round(minent, 4),
        'bit_ratio': ratio,
        'nist_passed': nist_passed
    }
