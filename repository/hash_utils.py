import hashlib

# Funzione hash semplificata (solo primi k bit)
def simple_hash(data: str, k: int) -> str:
    digest = hashlib.sha256(data.encode()).hexdigest()
    # Prendi solo k bit → k/4 caratteri hex
    return digest[:k // 4]
