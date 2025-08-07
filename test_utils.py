import rsa

def generate_test_keys():
    return rsa.newkeys(512)  # (pubkey, privkey)