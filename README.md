# Binance Futures Order Bot

A **CLI-based trading bot** supporting limit and market orders with robust **logging feature, and documentation**.  

> **Note:** Advanced features like TWAP and OCO are planned but not yet implemented.

---

## Features

### ✅ Core Orders
- **Market Orders** – Buy or sell instantly at the current market price.  
- **Limit Orders** – Buy or sell at a specific price.  


### 🛡 Logging
- Structured logging in `bot.log` with **timestamps** and **error traces**.  

---

## Installation

1. Clone the repository:

```bash
git clone https://github.com/dhrruvchotai/Dhruv-Binance-Bot.git
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

- Create a .env file:

```bash
API_KEY=your_api_key_here
API_SECRET=your_api_secret_here
```

4. Usage: 
- **Market Order**

```bash
python market_orders.py
```
Then enter the details for market order.

- **Limit Order**

```bash
python limit_orders.py
```
Then enter details for the limit orders.


5. Logging
- **All actions and errors are logged in bot.log:**
```bash
2025-10-04 08:51:11,063 - INFO - Market order: {'symbol': 'ETHUSDT', 'orderId': 297300, 'orderListId': -1, 'clientOrderId': 'x-HNA2TXFJ6923ff5f84d677085528b', 'transactTime': 1759548071010, 'price': '0.00000000', 'origQty': '1.00000000', 'executedQty': '1.00000000', 'origQuoteOrderQty': '0.00000000', 'cummulativeQuoteQty': '4482.81000000', 'status': 'FILLED', 'timeInForce': 'GTC', 'type': 'MARKET', 'side': 'BUY', 'workingTime': 1759548071010, 'fills': [{'price': '4482.81000000', 'qty': '1.00000000', 'commission': '0.00000000', 'commissionAsset': 'ETH', 'tradeId': 25330}], 'selfTradePreventionMode': 'EXPIRE_MAKER'}
2025-10-04 08:58:55,409 - INFO - Limit order: {'symbol': 'ETHUSDT', 'orderId': 297798, 'orderListId': -1, 'clientOrderId': 'x-HNA2TXFJ694349a562923689f1bf2', 'transactTime': 1759548535345, 'price': '2000.00000000', 'origQty': '1.00000000', 'executedQty': '0.00000000', 'origQuoteOrderQty': '0.00000000', 'cummulativeQuoteQty': '0.00000000', 'status': 'NEW', 'timeInForce': 'GTC', 'type': 'LIMIT', 'side': 'BUY', 'workingTime': 1759548535345, 'fills': [], 'selfTradePreventionMode': 'EXPIRE_MAKER'}
2025-10-04 08:59:18,770 - ERROR - Market order error: APIError(code=-2010): Account has insufficient balance for requested action.
```
 
6.Project Structure
```bash
[project_root]/
│
├── src/
│   ├── market_orders.py       # Market order logic
│   ├── limit_orders.py        # Limit order logic
│   ├── bot.log                # Logs of orders, errors, executions
│   └── advanced/
│       ├── oco.py  
│       └── twap.py        
│                 
├── README.md                  # Project documentation
└── report.pdf                 # Screenshots, analysis, explanations
```