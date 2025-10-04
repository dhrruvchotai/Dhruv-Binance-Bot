from binance import Client
from dotenv import load_dotenv
import os
import logging

load_dotenv()

logging.basicConfig(filename="bot.log", level=logging.INFO, format="%(asctime)s - %(levelname)s - %(message)s")

API_KEY = os.getenv("BINANCE_API_KEY")
API_SECRET = os.getenv("BINANCE_API_SECRET")

client = Client(API_KEY, API_SECRET, testnet=True)

def place_limit_order():
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
    price = float(input("Enter price: "))

    try:
        order = client.order_limit(
            symbol=symbol,
            side=side,
            type="LIMIT",
            timeInForce="GTC",
            quantity=qty,
            price=price
        )
        print("✅ Limit order placed:", order)
        logging.info(f"Limit order: {order}")
    except Exception as e:
        print("❌ Error:", e)
        logging.error(f"Limit order error: {e}")

if __name__ == "__main__":
    place_limit_order()
