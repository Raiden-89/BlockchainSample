from repository.block import Block
from repository.hash_utils import simple_hash

class Blockchain:
    def __init__(self, genesis_hash):
        self.blocks = []
        self.genesis_hash = genesis_hash

    def add_block(self, merkle_root, k):
        prev_hash = self.blocks[-1].block_hash if self.blocks else self.genesis_hash
        block = Block(prev_hash, merkle_root, k)
        self.blocks.append(block)

    def is_valid(self, k):
        prefix = '0' * (k // 4 // 2)
        prev_hash = self.genesis_hash

        for block in self.blocks:
            #controllo tra blocchi
            #Verifica che la lista self.blocks sia una sequenza ininterrotta, e che ogni block.prev_hash corrisponda esattamente al block_hash del blocco precedente
            if block.prev_hash != prev_hash:
                return False

            combined = block.prev_hash + block.merkle_root + block.nonce
            expected_hash = simple_hash(combined, k)
            if expected_hash != block.block_hash or not block.block_hash.startswith(prefix):
                return False
            prev_hash = block.block_hash

        return True

