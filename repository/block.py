from repository.hash_utils import simple_hash
import rsa
import time

class Block:
    def __init__(self, prev_hash, merkle_root, k, private_key):
        self.k = k
        self.prev_hash = prev_hash
        self.merkle_root = merkle_root
        self.timestamp = int(time.time())
        self.nonce, self.block_hash = self._mine()

        # Firma coerente con il contenuto
        message = f"{self.prev_hash}{self.merkle_root}{self.nonce}{self.timestamp}"
        self.signature = rsa.sign(message.encode(), private_key, 'SHA-256')

    def _mine(self):
        prefix = '0' * (self.k // 4 // 2)
        i = 0
        while True:
            nonce = f"nonce_{i}"
            combined = self.prev_hash + self.merkle_root + nonce + str(self.timestamp)
            h = simple_hash(combined, self.k)
            if h.startswith(prefix):
                return nonce, h
            i += 1

    def to_dict(self):
        return {
            "prev_hash": self.prev_hash,
            "merkle_root": self.merkle_root,
            "nonce": self.nonce,
            "block_hash": self.block_hash,
            "timestamp": self.timestamp,
            "signature": self.signature.hex()
        }
