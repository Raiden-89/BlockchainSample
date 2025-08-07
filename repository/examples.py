from repository.merkle_tree import MerkleTree
from repository.blockchain import Blockchain
import random
import string

def random_string(length=12):
    return ''.join(random.choices(string.ascii_letters + string.digits, k=length))

def run_demo(k):
    if k < 8:
        raise ValueError("Parametro k troppo basso: insicuro")
    sourceblock = random_string(3 * k)
    print(f"Sourceblock (genesis): {sourceblock}")

    chain = Blockchain(genesis_hash=sourceblock)

    for i in range(3):
        leaves = [random_string(6) for _ in range(4)]
        mtree = MerkleTree(leaves, k)
        chain.add_block(mtree.get_root(), k)

    print("Blockchain is valid?", chain.is_valid(k))
    for i, block in enumerate(chain.blocks):
        print(f"Block {i+1}:", block.to_dict())
