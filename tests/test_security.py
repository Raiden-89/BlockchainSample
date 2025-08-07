from repository.merkle_tree import MerkleTree
from repository.blockchain import Blockchain
from repository.hash_utils import simple_hash
import pytest

def test_blockchain_detect_prev_hash_tamper():
    # Step 1: crea una blockchain valida con 2 blocchi
    chain = Blockchain(genesis_hash="GEN")

    tree1 = MerkleTree(["a", "b"], k=8)
    chain.add_block(tree1.get_root(), k=8)

    tree2 = MerkleTree(["c", "d"], k=8)
    chain.add_block(tree2.get_root(), k=8)

    # Verifica che la blockchain sia valida PRIMA della manomissione
    assert chain.is_valid(k=8)

    # Step 2: manomette il prev_hash del blocco 0
    chain.blocks[0].prev_hash = "tampered_hash"

    # Step 3: ricontrolla la validità — ora deve fallire
    assert not chain.is_valid(k=8)


def test_nonce_correctness():
    # Crea un Merkle tree valido
    tree = MerkleTree(["alpha", "beta"], k=8)

    # Crea una blockchain e aggiungi il blocco
    chain = Blockchain(genesis_hash="g")
    chain.add_block(tree.get_root(), k=8)

    # Recupera il blocco appena aggiunto
    block = chain.blocks[0]

    # ✅ Verifica che l'hash del blocco inizi con '0' → vincolo imposto dal proof-of-work con k=8
    assert block.block_hash.startswith("0")

    # ✅ Verifica che l'hash del blocco sia calcolato correttamente
    combined = block.prev_hash + block.merkle_root + block.nonce

    # ⚠️ Usa __import__ per accedere dinamicamente a simple_hash da hash_utils
    assert block.block_hash == __import__("repository.hash_utils", fromlist=[""]).simple_hash(combined, 8)

def test_invalid_merkle_root():
    tree = MerkleTree(["a", "b"], k=8)
    tree.leaves[0] = "corrupted"
    assert not tree.validate()


def test_modifica_block_data():
    chain = Blockchain("GEN")
    tree = MerkleTree(["a", "b"], k=8)
    chain.add_block(tree.get_root(), k=8)

    # Modifica interna malevola (cambia la radice del Merkle tree)
    chain.blocks[0].merkle_root = "xxxx"

    # Deve fallire
    assert not chain.is_valid(k=8)

def test_block_rejects_weak_hash_length():
    """
    Verifica che la creazione di un Merkle Tree con k troppo basso venga rifiutata
    (k=4 → 1 solo hex char = solo 16 valori possibili → insicuro)
    """
    with pytest.raises(ValueError):
        MerkleTree(["a", "b"], k=4)  # Deve fallire se protezione presente


def test_detects_merkle_root_tampering():
    """
    Simula un attacco: modifica la radice del Merkle Tree in un blocco esistente.
    Deve rompere la validità della blockchain.
    """
    chain = Blockchain(genesis_hash="GEN")
    tree = MerkleTree(["x", "y"], k=8)
    chain.add_block(tree.get_root(), k=8)

    # Tampering: cambia la radice
    chain.blocks[0].merkle_root = "FAKE"

    assert not chain.is_valid(k=8)

def test_detects_nonce_tampering():
    """
    Simula un attacco: modifica il nonce del blocco. L'hash non sarà più coerente.
    """
    chain = Blockchain(genesis_hash="GEN")
    tree = MerkleTree(["1", "2"], k=8)
    chain.add_block(tree.get_root(), k=8)

    block = chain.blocks[0]
    block.nonce = "INVALID_NONCE"

    assert not chain.is_valid(k=8)


def test_detects_missing_block_in_chain():
    """
    Verifica che la rimozione di un blocco intermedio rompa la catena.
    """
    chain = Blockchain(genesis_hash="GEN")
    tree1 = MerkleTree(["a"], k=8)
    tree2 = MerkleTree(["b"], k=8)
    tree3 = MerkleTree(["c"], k=8)

    chain.add_block(tree1.get_root(), k=8)
    chain.add_block(tree2.get_root(), k=8)
    chain.add_block(tree3.get_root(), k=8)

    # Rimuove blocco 1 (il secondo blocco)
    chain.blocks.pop(1)

    # Ora la catena è "spezzata"
    assert not chain.is_valid(k=8)

def test_prev_hash_matches_previous_block():
    """
    Verifica che ogni blocco punti davvero al blocco precedente (via prev_hash).
    Se viene manomesso, deve fallire.
    """
    chain = Blockchain("GEN")
    t1 = MerkleTree(["X"], k=8)
    t2 = MerkleTree(["Y"], k=8)

    chain.add_block(t1.get_root(), k=8)
    chain.add_block(t2.get_root(), k=8)

    # Corrompe il prev_hash del secondo blocco
    chain.blocks[1].prev_hash = "FALSO_HASH"

    assert not chain.is_valid(k=8)
