from repository.merkle_tree import MerkleTree
from repository.blockchain import Blockchain
from repository.hash_utils import simple_hash
from test_utils import generate_test_keys  # Funzione che genera (pubkey, privkey) RSA

# TEST 1: rileva manomissione del prev_hash in un blocco
def test_blockchain_detect_prev_hash_tamper():
    # Genera chiavi RSA temporanee per il test
    pub, priv = generate_test_keys()

    # Crea una nuova blockchain con chiave pubblica per la verifica firme
    chain = Blockchain(genesis_hash="GEN", public_key=pub)

    # Crea due blocchi validi da aggiungere alla blockchain
    tree1 = MerkleTree(["a", "b"], k=8)
    chain.add_block(tree1.get_root(), k=8, private_key=priv)

    tree2 = MerkleTree(["c", "d"], k=8)
    chain.add_block(tree2.get_root(), k=8, private_key=priv)

    # Verifica che la blockchain sia valida prima della manomissione
    assert chain.is_valid(k=8)

    # ❌ Simula un attacco: modifica il prev_hash del primo blocco
    chain.blocks[0].prev_hash = "tampered_hash"

    # Dopo la modifica, la firma del secondo blocco non è più valida → la catena è rotta
    assert not chain.is_valid(k=8)


#  TEST 2: verifica che l'hash e la PoW siano coerenti con i dati firmati
def test_nonce_correctness():
    # Genera chiavi RSA
    pub, priv = generate_test_keys()

    # Crea un Merkle Tree semplice
    tree = MerkleTree(["alpha", "beta"], k=8)

    # Crea la blockchain e aggiungi un blocco valido
    chain = Blockchain(genesis_hash="g", public_key=pub)
    chain.add_block(tree.get_root(), k=8, private_key=priv)

    # Estrae il blocco aggiunto
    block = chain.blocks[0]

    # ✅ Verifica che l'hash generato rispetti il proof-of-work richiesto
    assert block.block_hash.startswith("0")

    # 🔄 Ricostruisce l'hash a partire dai campi del blocco
    combined = block.prev_hash + block.merkle_root + block.nonce + str(block.timestamp)

    # ✅ Verifica che l'hash calcolato coincida con quello salvato
    assert block.block_hash == simple_hash(combined, 8)
