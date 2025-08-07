from repository.hash_utils import simple_hash

class Block:
    def __init__(self, prev_hash: str, merkle_root: str, k: int):
        self.k = k
        self.prev_hash = prev_hash
        self.merkle_root = merkle_root
        self.nonce, self.block_hash = self._mine()

    def _mine(self):
        prefix = '0' * (self.k // 4 // 2)  # es. se k=8 → primi 4 bit = 1 hex char
        i = 0
        while True:
            nonce = f"nonce_{i}"
            combined = self.prev_hash + self.merkle_root + nonce
            h = simple_hash(combined, self.k)
            if h.startswith(prefix):
                return nonce, h
            i += 1

    def to_dict(self):
        return {
            "prev_hash": self.prev_hash,
            "merkle_root": self.merkle_root,
            "nonce": self.nonce,
            "block_hash": self.block_hash
        }
