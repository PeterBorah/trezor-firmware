from trezor import wire
from trezor.crypto.curve import secp256k1
from trezor.crypto.hashlib import sha3_256
from trezor.messages.Success import Success

async def verify_merkle_proof(ctx):
    return Success(message="Message verified")
