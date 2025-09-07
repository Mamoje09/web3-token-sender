import os
from dotenv import load_dotenv
from web3 import Web3

load_dotenv()

provider = os.getenv("WEB3_PROVIDER")
private_key = os.getenv("PRIVATE_KEY")
wallet_address = os.getenv("WALLET_ADDRESS")
usdc_contract_address = os.getenv("USDC_CONTRACT")

if not provider or not private_key or not wallet_address:
    raise SystemExit("❌ Please set WEB3_PROVIDER, PRIVATE_KEY, and WALLET_ADDRESS in .env")

w3 = Web3(Web3.HTTPProvider(provider))

def send_eth(to_address, amount_eth):
    nonce = w3.eth.get_transaction_count(wallet_address)
    tx = {
        "nonce": nonce,
        "to": to_address,
        "value": w3.to_wei(amount_eth, "ether"),
        "gas": 21000,
        "gasPrice": w3.eth.gas_price,
    }
    signed_tx = w3.eth.account.sign_transaction(tx, private_key)
    tx_hash = w3.eth.send_raw_transaction(signed_tx.raw_transaction)
    print(f"✅ Sent {amount_eth} ETH → {to_address}")
    print(f"🔗 Tx Hash: {w3.to_hex(tx_hash)}")

def send_usdc(to_address, amount_usdc):
    abi = [
        {
            "constant": False,
            "inputs": [
                {"name": "_to", "type": "address"},
                {"name": "_value", "type": "uint256"}
            ],
            "name": "transfer",
            "outputs": [{"name": "", "type": "bool"}],
            "type": "function",
        }
    ]
    contract = w3.eth.contract(address=usdc_contract_address, abi=abi)
    nonce = w3.eth.get_transaction_count(wallet_address)

    decimals = 6  # USDC uses 6 decimals
    amount = int(amount_usdc * (10 ** decimals))

    tx = contract.functions.transfer(to_address, amount).build_transaction({
        "nonce": nonce,
        "gas": 100000,
        "gasPrice": w3.eth.gas_price,
        "from": wallet_address
    })
    signed_tx = w3.eth.account.sign_transaction(tx, private_key)
    tx_hash = w3.eth.send_raw_transaction(signed_tx.raw_transaction)
    print(f"✅ Sent {amount_usdc} USDC → {to_address}")
    print(f"🔗 Tx Hash: {w3.to_hex(tx_hash)}")

if __name__ == "__main__":
    # DEMO VALUES (replace with real)
    recipient = "0xRecipientAddressHere"
    send_eth(recipient, 0.001)
    send_usdc(recipient, 5)
