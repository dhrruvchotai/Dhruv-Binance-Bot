# Binance Futures Order Bot

A **CLI-based trading bot** supporting limit and market orderswith robust **logging feature, and documentation**.  

> **Note:** Advanced features like TWAP and OCO are planned but not yet implemented.

---

## Features

### ✅ Core Orders (Implemented)
- **Market Orders** – Buy or sell instantly at the current market price.  
- **Limit Orders** – Buy or sell at a specific price.  


### 🛡 Logging
- Structured logging in `bot.log` with **timestamps** and **error traces**.  

---

## Installation

1. Clone the repository:

```bash
git clone https://github.com/[your_username]/[your_name]-binance-bot.git
```

2. Now follow this commands:

```bash
cd Dhruv-Binance-Bot

python -m venv venv

# Windows
venv\Scripts\activate
# macOS/Linux
source venv/bin/activate

pip install -r requirements.txt
```

3. Setup : 
- Obtain **Binance API Key** and **API Secret** from **https://testnet.binance.vision**.

- Create a .env file in /src:

```bash
API_KEY=your_api_key_here
API_SECRET=your_api_secret_here
```

4. Usage: 
- **Market Order**

```bash
python market_orders.py
```
- Now enter the details for market order

- **Limit Order**

```bash
python limit_orders.py
```
 
 

