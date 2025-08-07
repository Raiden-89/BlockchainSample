
from repository.merkle_tree import MerkleTree
from repository.blockchain import Blockchain
import random
import string

def random_string(length=6):
    return ''.join(random.choices(string.ascii_letters + string.digits, k=length))

def show_merkle_tree_example():
    print("\n ESEMPIO: Costruzione Merkle Tree")
    leaves = ["Alice", "Bob", "Charlie", "Dave"]
    tree = MerkleTree(leaves, k=8)
    print("Foglie:", leaves)
    print("Radice Merkle:", tree.get_root())
    print("Valido:", tree.validate())

    # Visualizzazione testuale dell'albero
    print("\nVisualizzazione Merkle Tree:")
    level = 0
    width = 4
    total = len(tree.tree)
    while width > 0:
        start = total - width
        end = total
        print(f" Livello {level}: ", tree.tree[start:end])
        total -= width
        width = width // 2
        level += 1

def show_blockchain_example():
    print("\n ESEMPIO: Costruzione Blockchain")
    chain = Blockchain(genesis_hash="GENESIS")

    for i in range(3):
        tx = [random_string() for _ in range(4)]
        tree = MerkleTree(tx, k=8)
        print(f"Blocco {i+1} - Transazioni: {tx}")
        chain.add_block(tree.get_root(), k=8)

    print("\nBlockchain valida?", chain.is_valid(k=8))

def show_attack_example():
    print("\n ESEMPIO: Simulazione di attacco")
    chain = Blockchain("GEN")
    t1 = MerkleTree(["X", "Y"], k=8)
    t2 = MerkleTree(["Z", "W"], k=8)

    chain.add_block(t1.get_root(), k=8)
    chain.add_block(t2.get_root(), k=8)

    print("Validità iniziale:", chain.is_valid(k=8))

    print("Modifico il prev_hash del secondo blocco...")
    chain.blocks[1].prev_hash = "HACKED"

    print("Validità dopo la manomissione:", chain.is_valid(k=8))

def main():
    print(" DEMO BLOCKCHAIN ")
    show_merkle_tree_example()
    show_blockchain_example()
    show_attack_example()

if __name__ == "__main__":
    main()
