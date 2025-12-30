Binance Futures Testnet Trading Bot (Python)


A simplified trading bot built using Python and the official Binance API.
This project allows users to place Market, Limit, and Stop-Limit (Bonus) 
orders on the Binance Futures Testnet (USDT-M) using a Command Line Interface
(CLI) and an optional Streamlit UI.


⚠️ This project uses Binance Futures Testnet only.
No real funds are involved.


📌 Features

Binance Futures Testnet integration
Market & Limit orders (BUY / SELL)
Bonus: Stop-Limit order support
CLI-based user input & validation
Optional Streamlit UI for easy interaction
Modular & reusable code structure
Proper logging & error handling


🧠 Tech Stack

Python 3
python-binance (official Binance library)
Streamlit (optional UI)
Binance Futures Testnet API


📂 Project Folder Structure
trading-bot/
│
├── main.py            → CLI entry point
├── ui.py              → Optional Streamlit UI
├── requirements.txt   → Project dependencies
├── README.md          → Documentation
├── .env               → API keys (not committed)
│
├── bot/
│   ├── basic_bot.py   → Binance client + leverage setup
│   ├── orders.py      → Order execution logic
│   ├── validator.py   → Input validation
│   └── logger.py      → Logging configuration
│
├── config/
│   └── settings.py    → Constants & configuration
│
└── logs/
    └── bot.log        → API requests, responses & errors


🔐 Binance Testnet Setup (Required)

Open: https://testnet.binancefuture.com
Login / Register
Generate API Key & Secret
Enable Futures trading permission
Add USDT balance using the Testnet Faucet


⚙️ Environment Setup

Install dependencies
pip install -r requirements.txt

Create .env file
BINANCE_API_KEY=your_testnet_api_key
BINANCE_API_SECRET=your_testnet_api_secret


▶️ How the Bot Works-----------------------
User
 │
 ▼
CLI / UI Input
 │
 ▼
Input Validation
 │
 ▼
Binance Client (Testnet)
 │
 ▼
Order Execution (Futures)
 │
 ▼
Response + Logs


🔄 Detailed Workflow------------------------

1️⃣ User Input
The user provides:
Trading symbol (e.g. BTCUSDT)
Order type (MARKET / LIMIT / STOP_LIMIT)
Order side (BUY / SELL)
Quantity
Price (if required)


2️⃣ Validation Layer
Before making any API call:
Symbol is validated
Order type is verified
Quantity & price are checked

❌ Invalid input → execution stops
✅ Valid input → request continues


3️⃣ Binance Client Initialization
Client(api_key, api_secret)
Futures Testnet URL is applied
Default leverage is set (1x)



4️⃣ Order Execution Logic
MARKET      → Immediate execution
LIMIT       → Executed when price matches
STOP_LIMIT  → Trigger-based execution (Bonus)


Note: Each order type is handled by a separate function to maintain clean and reusable code.


5️⃣ Logging
All critical events are logged:
API requests
Order execution attempts
Errors (if any)
Logs are stored in:
logs/bot.log


Order Flow Diagrams (Beginner Friendly)

MARKET Order
User
 │
 ▼
Market Order Request
 │
 ▼
Binance Testnet
 │
 ▼
Immediate Execution

LIMIT Order
User
 │
 ▼
Limit Order (Price specified)
 │
 ▼
Binance Order Book
 │
 ▼
Executed when price matches

STOP-LIMIT Order (Bonus)
Market Price
 │
 ▼
Stop Price Triggered
 │
 ▼
Limit Order Placed
 │
 ▼
Execution on price match


🖥️ CLI Usage
Run the bot:
python main.py

Example:
Enter Symbol: BTCUSDT
Enter Order Type: MARKET
Enter Side: BUY
Enter Quantity: 0.001


🌐 Optional Streamlit UI

Run the UI:
streamlit run ui.py
UI Features
Dropdown selection for order types
Input fields for symbol, quantity, and price
Button-based order execution
JSON response display

The Streamlit UI is optional and added for demonstration purposes only.


⚠️ Important Testnet Notes
Binance Futures Testnet may return:
orderId = None

This is a known Testnet limitation

Orders may still be accepted internally

✔ The application handles this gracefully
✔ Logs capture full request and response details


👨‍💻 Author
Rahul Kumar
MCA Graduate | Python & Backend Developer