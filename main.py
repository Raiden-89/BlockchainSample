import rsa
import random
import string
from repository.merkle_tree import MerkleTree
from repository.blockchain import Blockchain
from keys import load_keys

#  Carica le chiavi salvate
pubkey, privkey = load_keys()

def random_string(length=6):
    return ''.join(random.choices(string.ascii_letters + string.digits, k=length))

def show_merkle_tree_example():
    print("\n ESEMPIO: Costruzione Merkle Tree")
    leaves = ["Alice", "Bob", "Charlie", "Dave"]
    tree = MerkleTree(leaves, k=8)
    print("Foglie:", leaves)
    print("Radice Merkle:", tree.get_root())
    print("Valido:", tree.validate())

def show_blockchain_example(pubkey, privkey):
    print("\n ESEMPIO: Costruzione Blockchain con firme digitali")
    chain = Blockchain(genesis_hash="GENESIS", public_key=pubkey)

    for i in range(3):
        tx = [random_string() for _ in range(4)]
        tree = MerkleTree(tx, k=8)
        print(f"Blocco {i+1} - Transazioni: {tx}")
        chain.add_block(tree.get_root(), k=8, private_key=privkey)

    print("\nBlockchain valida?", chain.is_valid(k=8))

def show_attack_example(pubkey, privkey):
    print("\n ESEMPIO: Simulazione di attacco con firma")
    chain = Blockchain("GEN", public_key=pubkey)
    t1 = MerkleTree(["X", "Y"], k=8)
    t2 = MerkleTree(["Z", "W"], k=8)

    chain.add_block(t1.get_root(), k=8, private_key=privkey)
    chain.add_block(t2.get_root(), k=8, private_key=privkey)

    print("Validità iniziale:", chain.is_valid(k=8))

    print("Modifico il prev_hash del secondo blocco...")
    chain.blocks[1].prev_hash = "HACKED"

    print("Validità dopo la manomissione:", chain.is_valid(k=8))

def main():
    print(" DEMO BLOCKCHAIN CON FIRME DIGITALI ")
    show_merkle_tree_example()
    show_blockchain_example(pubkey, privkey)
    show_attack_example(pubkey, privkey)

if __name__ == "__main__":
    main()
