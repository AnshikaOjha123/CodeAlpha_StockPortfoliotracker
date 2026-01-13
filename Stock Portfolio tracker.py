# Hardcoded stock prices
stock_prices = {
    "AAPL": 180,
    "TSLA": 250,
    "GOOGL": 140,
    "AMZN": 130,
    "MSFT": 310
}

print("📈 Welcome to Stock Portfolio Tracker")

total_investment = 0

while True:
    stock_name = input("\nEnter stock name (AAPL/TSLA/GOOGL/AMZN/MSFT) or 'done' to finish: ").upper()

    if stock_name == "DONE":
        break

    if stock_name not in stock_prices:
        print("❌ Stock not found. Try again.")
        continue

    try:
        quantity = int(input("Enter quantity: "))
    except ValueError:
        print("❌ Please enter a valid number.")
        continue

    investment = stock_prices[stock_name] * quantity
    total_investment += investment

    print(f"✅ {stock_name} added | Investment: ${investment}")

print("\n💰 Total Portfolio Value: $", total_investment)

with open("portfolio.txt", "w") as file:
    file.write(f"Total Portfolio Value: ${total_investment}")

print("📁 Portfolio value saved in portfolio.txt")