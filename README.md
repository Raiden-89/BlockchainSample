
# 🧱 Blockchain Demo Project 

Questo progetto è una **dimostrazione didattica** del funzionamento di una semplice blockchain, costruita in Python. Include:
- Hash function semplificata
- Merkle Tree
- Blockchain con proof-of-work
- Validazione e test di sicurezza

---

## 📂 Struttura del progetto

```
.
├── repository/
│   ├── hash_utils.py         # Funzione hash personalizzata
│   ├── merkle_tree.py        # Costruzione e validazione del Merkle Tree
│   ├── block.py              # Blocco con proof-of-work
│   ├── blockchain.py         # Catena di blocchi e validazione
│   ├── examples.py           # Esecuzione dimostrativa
│   └── main.py               # Punto di ingresso
├── tests/
│   ├── test_merkle.py        # Test sul Merkle Tree
│   ├── test_blockchain.py    # Test sulla Blockchain
│   ├── test_security.py      # Test di sicurezza avanzati
├── requirements.txt
└── README.md
```

---

## 🚀 Come eseguire

1. Clona o scarica il progetto
2. Installa i requirements:
   ```bash
   pip install -r requirements.txt
   ```
3. Esegui il demo:
   ```bash
   python repository/main.py
   ```
4. Lancia tutti i test:
   ```bash
   pytest tests/
   ```

---

## 🧩 Componenti principali

### 🔐 `hash_utils.py`
- Funzione `simple_hash(data, k)` che restituisce solo i primi `k` bit dell'hash SHA256.
- Usata per simulare funzioni hash semplificate e testare proof-of-work.

### 🌳 `merkle_tree.py`
- Costruisce un **Merkle Tree** dalle foglie (transazioni).
- Calcola la **radice** combinando gli hash delle coppie.
- Metodo `.validate()` ricostruisce la radice per garantire l'integrità.

### 📦 `block.py`
- Classe `Block`: contiene `prev_hash`, `merkle_root`, `nonce` e `block_hash`.
- Usa `proof-of-work` (PoW): trova un nonce tale che l'hash inizi con `k/2` zeri.

### 🔗 `blockchain.py`
- Costruisce e valida una catena di blocchi.
- Controlla:
  - Collegamento tra blocchi (`prev_hash == block_precedente.block_hash`)
  - Validità della PoW
  - Integrità dei dati

---

## 🛡️ Sicurezza

Il file `test_security.py` include test che rilevano:
- ❌ Modifica del `prev_hash`
- ❌ Modifica della `merkle_root`
- ❌ Modifica del `nonce`
- ❌ Hash troppo corti (es. `k=4`)
- ❌ Rimozione o corruzione dei blocchi intermedi

---

## 📚 Esempi di output

```
Sourceblock (genesis): wOsWUxog34yDD2aF1DJS0UI4
Blockchain is valid? True
Block 1: {'prev_hash': 'wOsWUxog34yDD2aF1DJS0UI4', 'merkle_root': '0f', 'nonce': 'nonce_9', 'block_hash': '01'}
Block 2: {'prev_hash': '01', 'merkle_root': '36', 'nonce': 'nonce_9', 'block_hash': '0f'}
Block 3: {'prev_hash': '0f', 'merkle_root': 'e2', 'nonce': 'nonce_22', 'block_hash': '0e'}
```

---

## ✅ Obiettivi 

- Capire la struttura di una blockchain reale
- Applicare funzioni hash e Merkle tree
- Simulare PoW in ambienti controllati
- Scrivere test di sicurezza per identificare vulnerabilità

---


