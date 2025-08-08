
# 🧠 Blockchain Didattica con Firma Digitale e Tracciabilità

Questo progetto è una simulazione di una **blockchain**, scritta in Python.  
Incorpora concetti reali come **Merkle Tree**, **Proof-of-Work**, **firme digitali RSA** e una **dashboard interattiva** per la tracciabilità nella supply chain farmaceutica.

---

## 🚀 Funzionalità principali

- 🌳 Merkle Tree per integrità dei dati
- 🔐 Firma digitale RSA dei blocchi
- ⛏️ Proof-of-Work configurabile (`k`)
- 🔗 Validazione completa della blockchain
- 📦 Tracciabilità eventi in ambito farmaceutico (Streamlit)
- 🧪 Test automatici per validità e sicurezza

---

## 🗂️ Struttura del progetto

```
BlockchainSample/
├── repository/
│   ├── block.py              # Definizione blocco con firma + PoW
│   ├── blockchain.py         # Validazione della catena
│   ├── hash_utils.py         # SHA-256 semplificato
│   ├── merkle_tree.py        # Albero di Merkle
│   ├── examples.py           # Demo integrativa
│   └── __init__.py
│
├── tests/                    # Suite Pytest
│   ├── test_blockchain.py
│   ├── test_merkle.py
│   ├── test_security.py
│
├── keys/                     # Chiavi RSA (generabili)
│   ├── public.pem
│   └── private.pem
│
├── main.py                   # Demo CLI
├── keys.py                   # Generatore/caricatore chiavi
├── test_utils.py             # Supporto test (chiavi fake)
├── pharma_blockchain_app.py  # UI interattiva Streamlit
├── requirements.txt
└── README.md
```

---

## ✅ Come iniziare

### 1. Installa le dipendenze
```bash
pip install -r requirements.txt
```

### 2. Genera le chiavi RSA
```bash
python keys.py
```

### 3. Avvia la demo CLI
```bash
python main.py
```

### 4. Avvia la dashboard farmaceutica
```bash
streamlit run pharma_blockchain_app.py
```

### 5. Esegui i test
```bash
pytest
```

---

## 💊 Caso d'uso: Tracciabilità Farmaceutica

Con `pharma_blockchain_app.py` puoi:
- Registrare eventi della catena logistica farmaceutica
- Ogni evento è convertito in un Merkle Tree e inserito in un blocco
- Ogni blocco è firmato con una chiave RSA e collegato al precedente
- La validità dell'intera catena può essere verificata in tempo reale
- Puoi esportare i blocchi in un file JSON

---

## 🔐 Sicurezza e validazioni

- 🔁 Verifica hash dei blocchi (PoW)
- 📎 Verifica firma digitale (RSA)
- ⛔ Rileva modifiche non autorizzate (es. tampering)
- 🔍 Protezione da blocchi con difficoltà troppo bassa (`k < 8`)
- 📄 Tutto è testato automaticamente con `pytest`

---

## 🧪 Esempi di test coperti

- Coerenza radice Merkle
- Blocco manomesso (hash o nonce)
- Firma non valida
- Rimozione di blocchi intermedi
- Prev_hash incoerente

---

## 📌 Requisiti

- Python 3.12+
- Librerie Python requirements.txt

---

## 📜 Licenza

Non è adatto per ambienti di produzione o uso critico senza adeguata revisione.

---


