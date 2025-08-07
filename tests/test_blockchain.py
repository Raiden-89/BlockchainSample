import pytest
from repository.merkle_tree import MerkleTree
from repository.blockchain import Blockchain
from test_utils import generate_test_keys  # Se la funzione è in un file separato

def test_blockchain_validity_chain():
    # Genera una coppia di chiavi RSA
    pub, priv = generate_test_keys()

    # Inizializza la blockchain con la chiave pubblica per la verifica
    chain = Blockchain(genesis_hash="gen", public_key=pub)

    # Crea un Merkle Tree con due transazioni e calcola la radice
    leaves = ["1", "2"]
    root = MerkleTree(leaves, k=8).get_root()

    # Aggiunge il blocco firmato alla blockchain
    chain.add_block(root, k=8, private_key=priv)

    # Verifica che la blockchain sia valida (PoW + firma + collegamenti)
    assert chain.is_valid(k=8)


def test_blockchain_invalid_hash():
    pub, priv = generate_test_keys()
    chain = Blockchain(genesis_hash="gen", public_key=pub)

    # Crea un blocco valido
    root = MerkleTree(["1", "2"], k=8).get_root()
    chain.add_block(root, k=8, private_key=priv)

    # ⚠Manomissione: modifica manualmente il block_hash
    chain.blocks[0].block_hash = "ffff"

    # Deve rilevare l'invalidità perché la firma e PoW non combaciano più
    assert not chain.is_valid(k=8)

def test_proof_of_work_tougher_difficulty():
    pub, priv = generate_test_keys()
    chain = Blockchain(genesis_hash="start", public_key=pub)

    # Crea un blocco con PoW più difficile (k=12 richiede più zeri)
    root = MerkleTree(["foo", "bar"], k=12).get_root()
    chain.add_block(root, k=12, private_key=priv)

    # Verifica che il blocco rispetti i requisiti di difficoltà
    assert chain.is_valid(k=12)

