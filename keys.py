import rsa
import os

KEYS_DIR = "keys"
PUBLIC_PATH = os.path.join(KEYS_DIR, "public.pem")
PRIVATE_PATH = os.path.join(KEYS_DIR, "private.pem")

def generate_keys():
    os.makedirs(KEYS_DIR, exist_ok=True)
    public_key, private_key = rsa.newkeys(512)
    with open(PUBLIC_PATH, "wb") as pub_file:
        pub_file.write(public_key.save_pkcs1())
    with open(PRIVATE_PATH, "wb") as priv_file:
        priv_file.write(private_key.save_pkcs1())
    print(" Chiavi RSA generate e salvate in 'keys/'")

def load_keys():
    with open(PUBLIC_PATH, "rb") as pub_file:
        public_key = rsa.PublicKey.load_pkcs1(pub_file.read())
    with open(PRIVATE_PATH, "rb") as priv_file:
        private_key = rsa.PrivateKey.load_pkcs1(priv_file.read())
    return public_key, private_key

if __name__ == "__main__":
    generate_keys()
