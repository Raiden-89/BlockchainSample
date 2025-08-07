import pytest
from repository.merkle_tree import MerkleTree
from repository.blockchain import Blockchain


def test_blockchain_validity_chain():
    # Crea una nuova blockchain con un hash iniziale 'gen'
    chain = Blockchain(genesis_hash="gen")

    # Crea un Merkle tree con due foglie "1" e "2" e calcola la radice
    leaves = ["1", "2"]
    root = MerkleTree(leaves, k=8).get_root()

    # Aggiunge il blocco alla blockchain con proof-of-work (k=8 → bassa difficoltà)
    chain.add_block(root, k=8)

    # Verifica che la blockchain sia valida (nessuna manomissione)
    assert chain.is_valid(k=8)

def test_blockchain_invalid_hash():
    # Crea una nuova blockchain con un hash iniziale
    chain = Blockchain(genesis_hash="gen")

    # Crea un Merkle tree con due foglie
    leaves = ["1", "2"]
    root = MerkleTree(leaves, k=8).get_root()

    # Aggiunge un blocco valido alla blockchain
    chain.add_block(root, k=8)

    # MANOMISSIONE: sovrascrive l'hash del blocco con un valore arbitrario
    chain.blocks[0].block_hash = "ffff"

    # Verifica che la blockchain NON sia più valida
    assert not chain.is_valid(k=8)


def test_proof_of_work_tougher_difficulty():
    # Crea una blockchain con hash iniziale 'start'
    chain = Blockchain(genesis_hash="start")

    # Crea un Merkle tree con due foglie
    leaves = ["foo", "bar"]
    root = MerkleTree(leaves, k=12).get_root()

    # Aggiunge un blocco con una difficoltà maggiore (k=12 → più zeri iniziali)
    chain.add_block(root, k=12)

    # Verifica che la proof-of-work soddisfi le condizioni di validità
    assert chain.is_valid(k=12)

