
import rsa
from repository.block import Block
from repository.hash_utils import simple_hash

class Blockchain:
    def __init__(self, genesis_hash, public_key):
        self.blocks = []
        self.genesis_hash = genesis_hash
        self.public_key = public_key

    def add_block(self, merkle_root, k, private_key):
        prev_hash = self.blocks[-1].block_hash if self.blocks else self.genesis_hash
        block = Block(prev_hash, merkle_root, k, private_key)
        self.blocks.append(block)

    def is_valid(self, k):
        prefix = '0' * (k // 4 // 2)
        prev_hash = self.genesis_hash

        for block in self.blocks:
            # 1. Controlla coerenza prev_hash
            if block.prev_hash != prev_hash:
                return False

            # 2. Ricostruisce hash
            combined = block.prev_hash + block.merkle_root + block.nonce + str(block.timestamp)
            expected_hash = simple_hash(combined, k)

            # 3. Controlla PoW
            if expected_hash != block.block_hash or not block.block_hash.startswith(prefix):
                return False

            # 4. Verifica firma
            try:
                rsa.verify(combined.encode(), block.signature, self.public_key)
            except rsa.VerificationError:
                return False

            prev_hash = block.block_hash

        return True
