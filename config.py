import binascii

# used for derivation of per-tag keys
DERIVE_MODE = "legacy"
MASTER_KEY = binascii.unhexlify("4A9F2E8B1C7D3E6A5B0F4C2D9E8A1B3F")

# for encrypted mirroring
ENC_PICC_DATA_PARAM = "picc_data"
ENC_FILE_DATA_PARAM = "enc"

# for plaintext mirroring
UID_PARAM = "uid"
CTR_PARAM = "ctr"

# always applied
SDMMAC_PARAM = "cmac"

# accept only SDM using LRP, disallow usage of AES
REQUIRE_LRP = False
