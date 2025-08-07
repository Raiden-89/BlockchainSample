import pytest
from repository.merkle_tree import MerkleTree

def test_merkle_tree_root_consistency():
    # Crea due alberi Merkle identici con le stesse foglie
    leaves = ["a", "b", "c", "d"]
    tree1 = MerkleTree(leaves, k=8)
    tree2 = MerkleTree(leaves, k=8)

    # Verifica che le due radici calcolate siano uguali
    # Questo conferma che la costruzione dell'albero è deterministica
    assert tree1.get_root() == tree2.get_root()

def test_merkle_tree_single_leaf():
    # Crea un Merkle tree con una sola foglia
    leaves = ["only"]
    tree = MerkleTree(leaves, k=8)

    # In questo caso, la radice deve coincidere con l'unico hash della foglia
    assert tree.get_root() == tree.leaves[0]


def test_merkle_validate_tamper():
    # Crea un Merkle tree con due foglie
    leaves = ["x", "y"]
    tree = MerkleTree(leaves, k=8)

    # MANOMISSIONE: modifica direttamente una foglia dell'albero
    tree.leaves[0] = "tampered"

    # La validazione deve fallire, poiché la struttura è stata alterata
    assert not tree.validate()
