# Ethereum Token Sender 🚀

A Python tool to send **ETH** or **ERC-20 tokens (USDC)** to another wallet.  
Built with **Web3.py** and Infura RPC.  

---

## ⚠️ Warning
This script **broadcasts real transactions**.  
- Only use **testnets** (e.g., Sepolia) until you are confident.  
- Never commit your `.env` with private keys.  

---

## ✨ Features
- ✅ Send ETH directly from your wallet  
- ✅ Send USDC (ERC-20) with correct decimals  
- ✅ Outputs transaction hash & explorer link  
- ✅ Configurable via `.env`  
- ✅ CLI support: choose recipient, amount and token type  


---

## 📂 Project Structure

web3_token_sender/
├── send_token.py # Main script

├── requirements.txt # Dependencies

├── README.md # Documentation

└── .env # Local environment variables (ignored by Git)

---

▶️ Usage (CLI)

Send ETH

python send_token.py 0xRecipientAddress 0.01 ETH

Send USDC

python send_token.py 0xRecipientAddress 5 USDC

---

✅ Output:

✅ Sent 0.01 ETH → 0xRecipient

🔗 Tx Hash: 0x123abc...

✅ Sent 5.0 USDC → 0xRecipient

🔗 Tx Hash: 0x456def...

---

📸 Demo Output

Console output (ETH + USDC transfers)

Etherscan confirmation screenshots

---

🛠 Roadmap

Add support for multiple ERC-20 tokens

Add ERC-721 (NFT) transfers

Interactive CLI (choose token + amount without arguments)

Optional web dashboard

---

📬 About Me

I’m Mamo (GitHub: mamoje09
I,m a backend engineer expanding into Web3.
This is my third Web3 project, showing I can not only read blockchain data but also send transactions programmatically with a professional CLI tool.



---

## ⚙️ Setup

### 1. Clone the repo
```bash
git clone https://github.com/mamoje09/web3-token-sender.git
cd web3-token-sender


 
