
import streamlit as st
import rsa
import os
import json
from repository.merkle_tree import MerkleTree
from repository.blockchain import Blockchain
from keys import load_keys

st.set_page_config(page_title="Blockchain Tracciabilità Farmaceutica", layout="centered")

st.title("💊 Blockchain per la Tracciabilità Farmaceutica")

# Carica chiavi RSA
if not os.path.exists("keys/public.pem") or not os.path.exists("keys/private.pem"):
    st.error("Chiavi RSA mancanti. Esegui prima keys.py per generarle.")
    st.stop()

pubkey, privkey = load_keys()

# Inizializza la blockchain
if "chain" not in st.session_state:
    st.session_state.chain = Blockchain("PHARMA_CHAIN_START", public_key=pubkey)
    st.session_state.k = 8

# Inserimento dati del blocco
st.subheader("➕ Registra un nuovo evento nella supply chain farmaceutica")
med_name = st.text_input("Nome del farmaco", "Paracetamolo 500mg")
batch_id = st.text_input("Lotto di produzione", "BATCH2025A")
event_type = st.selectbox("Fase della supply chain", ["Produzione", "Controllo qualità", "Trasporto", "Stoccaggio", "Distribuzione", "Somministrazione"])
location = st.text_input("Luogo", "Stabilimento di Roma")
operator = st.text_input("Operatore responsabile", "Operatore 001")
timestamp = st.text_input("Data/ora evento", "2025-08-07 12:00")

if st.button("✅ Aggiungi evento alla blockchain"):
    foglie = [med_name, batch_id, event_type, location, operator, timestamp]
    tree = MerkleTree(foglie, k=st.session_state.k)
    root = tree.get_root()

    st.session_state.chain.add_block(root, k=st.session_state.k, private_key=privkey)
    st.success("Evento registrato correttamente nella blockchain!")

# Visualizzazione catena
st.subheader("🔗 Registro Blockchain degli eventi")

if len(st.session_state.chain.blocks) == 0:
    st.info("Nessun evento ancora registrato.")
else:
    for i, block in enumerate(st.session_state.chain.blocks):
        with st.expander(f"🧬 Blocco {i+1}"):
            st.json(block.to_dict())

    valid = st.session_state.chain.is_valid(k=st.session_state.k)
    st.markdown(f"🛡️ Stato della catena: **{'Valida ✅' if valid else 'Non valida ❌'}**")

# Esportazione in JSON
if st.button("💾 Esporta Blockchain in JSON"):
    data = [b.to_dict() for b in st.session_state.chain.blocks]
    with open("pharma_blockchain.json", "w") as f:
        json.dump(data, f, indent=2)
    st.success("Esportata in 'pharma_blockchain.json'")
