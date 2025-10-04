from binance import Client
from dotenv import load_dotenv
import os
import logging
import time

load_dotenv()

# Logging setup
logging.basicConfig(filename="bot.log", level=logging.INFO, format="%(asctime)s - %(levelname)s - %(message)s")

API_KEY = os.getenv("BINANCE_API_KEY")
API_SECRET = os.getenv("BINANCE_API_SECRET")

print("API_KEY:", API_KEY)
print("API_SECRET:", API_SECRET)

client = Client(API_KEY, API_SECRET, testnet=True)

# account =  client.get_account()
# print("USER ACCOUNT : ",account)

def place_market_order():
    symbol = input("Enter symbol (e.g., BTCUSDT): ").upper()
    info = client.get_symbol_info(symbol)
    if not info:    
        print("❌ Invalid symbol.")
        return      
    min_qty = float(info['filters'][1]['minQty'])  
    max_qty = float(info['filters'][1]['maxQty'])     
    print(f"Minimum quantity to trade: {min_qty}")
    print(f"Maximum quantity to trade: {max_qty}")
    side = input("Enter side (BUY/SELL): ").upper()
    qty = float(input("Enter quantity: "))

    try:
        order = client.order_market_buy(
            symbol=symbol,
            side=side,
            type="MARKET",
            quantity=qty
        )
        print("✅ Market order placed:", order)
        logging.info(f"Market order: {order}")
    except Exception as e:
        print("❌ Error:", e)
        logging.error(f"Market order error: {e}")

if __name__ == "__main__":
    place_market_order()
